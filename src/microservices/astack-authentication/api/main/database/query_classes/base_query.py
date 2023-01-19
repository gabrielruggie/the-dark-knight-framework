from typing import Any, Dict, Generic, TypeVar, Type
from fastapi.encoders import jsonable_encoder
from main.database.session import Base
from main.schemas.schemas_response import Response
from pydantic import BaseModel
from sqlalchemy.orm import Session, Query

from loguru import logger
from passlib.hash import sha256_crypt

ModelType = TypeVar("ModelType", bound=Base)
NewRowSchemaType = TypeVar("NewRowSchemaType", bound=BaseModel)
UpdateExistingRowSchemaType = TypeVar("UpdateExistingRowSchemaType", bound=BaseModel)

'''
Generic class that requires the table, resource and update_resource schemas
'''
class BaseQuery (Generic[ModelType, NewRowSchemaType, UpdateExistingRowSchemaType]):
    def __init__ (self, model: Type[ModelType], tablename: str):
        self.model = model
        if self.model != None:
            self.model.__tablename__ =  tablename
        
        # Going to want to raise an error here

    # Session Query => SELECT <class.id> FROM <class.name>
    def get_resource_by_id (self, dk_session: Session, id: Any) -> Dict:

        logger.debug(f'Fetching resource with id: {id}')
        row_data = dk_session.query(self.model).filter(self.model.id == id).first()
        logger.debug(f'Found resource with data: {row_data}')

        return self.convert_row_data_to_dict(row=row_data)
    
    # Creates new resource in respective table based on the model and schema types
    def create_resource (self, dk_session: Session, resource: NewRowSchemaType) -> Response:

        resource_json = jsonable_encoder(resource)
        logger.debug(f'converting resource schema data to JSON: {resource_json}')
        # Expects a row of type <Base.class> to be inserted
        row = self.model(**resource_json)

        dk_session.add(row)
        dk_session.commit()
        dk_session.refresh(row)

        return Response(http_code=200, msg='Resource added to database')

    def convert_row_data_to_dict (self, row: Query) -> Dict:
        result = {}

        for column in row.__table__.columns:
            result[column.name] = str(getattr(row, column.name))
        
        return result 

'''
Given the correct schemas, this class will use the BaseQuery to build a query to send to DK
'''
class ConstructBaseQuery:

    def hash_password (self, password) -> str:
        return sha256_crypt.hash(password)
