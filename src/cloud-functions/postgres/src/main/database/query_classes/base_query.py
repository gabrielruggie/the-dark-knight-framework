from typing import Any, Dict, Generic, TypeVar, Type
from fastapi.encoders import jsonable_encoder
from main.database.session import Base
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
        dk_session.commit()
        logger.debug(f'Found resource with data: {row_data}')

        if row_data == None:
            return None
        
        return self.convert_row_data_to_dict(row=row_data)
    
    # Session Query => DELETE FROM <model.name> WHERE <resource.id> = <id>
    def delete_resource_by_id (self, dk_session: Session, id: Any) -> None:

        logger.debug(f'Deleting resource with id: {id}')
        dk_session.query(self.model).filter(self.model.id == id).delete()
        dk_session.commit()
        logger.debug('Successfully deleted resource from database')
    
    # Creates new resource in respective table based on the model and schema types
    def create_resource (self, dk_session: Session, resource: NewRowSchemaType) -> None:

        resource_json = jsonable_encoder(resource)
        logger.debug(f'converting resource schema data to JSON: {resource_json}')
        # Expects a row of type <Base.class> to be inserted
        row = self.model(**resource_json)

        dk_session.add(row)
        dk_session.commit()
        logger.debug(f'added new row to database')
        dk_session.refresh(row)


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
