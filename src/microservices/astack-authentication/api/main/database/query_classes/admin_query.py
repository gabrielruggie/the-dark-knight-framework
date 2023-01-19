from typing import Dict

from main.database.tables.table import Table
from main.database.query_classes.base_query import BaseQuery, ConstructBaseQuery
from main.schemas.schemas_admin import AdminDarkKnightDatabase, UpdateAdminDarkKnight, NewAdminDarkKnight

from loguru import logger
from sqlalchemy.orm import Session

'''
Uses generic class to build a query class for the Admin table in DK
Contains update query to update existing admin in DK
'''
class AdminQuery (BaseQuery[Table.Admin, AdminDarkKnightDatabase, UpdateAdminDarkKnight]):
    
    # Session Query => SELECT <class.id> FROM <class.name>
    # Overrides base class get resource method
    def get_resource_by_id (self, dk_session: Session, login_id: int) -> Dict:

        logger.debug(f'Fetching resource with id: {login_id}')
        row_data = dk_session.query(self.model).filter(self.model.login_id == login_id).first()
        logger.debug(f'Found resource with data: {row_data.__dict__}')

        return self.convert_row_data_to_dict(row=row_data)

    def update_admin_properties (self, dk_session: Session, admin: UpdateAdminDarkKnight):
        # Get this from JWT
        admin_id = admin.id
        
        try:

            logger.info(f'Updating user: {admin.username}')

            dk_session.\
                query(self.model).\
                    filter(self.model.id == admin_id).\
                        update(
                            {
                                "username": admin.username,
                                "position": admin.position,
                                "astack_right_level": admin.astack_right_level,
                                "email": admin.email
                            }
                        )
            dk_session.commit()

        except Exception as e:
            logger.debug(f'Could not update user: {admin["username"]}. Stopped by: {e}')

'''
Inherits base constructor class to construct a query for the admin table in DK
'''
class ConstructAdminQuery(ConstructBaseQuery):

    # Instantiates an AdminQuery object when this constructor class is instantiated
    def __init__ (self, dk_session: Session):
        self.session = dk_session
        self.admin_query = AdminQuery(Table.Admin, tablename='admin')
    
    # Adds aditional details to admin object before sending to DK
    # Basically, prepares our objects so there are no invalid properties 
    def add_dk_details (self, new_admin: NewAdminDarkKnight, unique_id: str, password: str) -> AdminDarkKnightDatabase:
        hashword = self.hash_password(password)

        logger.info("Creating new DK admin object")
        dk_admin = AdminDarkKnightDatabase(
            id=unique_id,
            login_id=new_admin.login_id,
            first_name=new_admin.first_name,
            last_name=new_admin.last_name,
            username=new_admin.username,
            email=new_admin.email,
            hashed_password=hashword,
            position=new_admin.position,
            astack_right_level=new_admin.astack_right_level
        )

        return dk_admin
    
    # Calls create_resource query to insert new admin to DK
    def insert_to_admin_table (self, admin: AdminDarkKnightDatabase):

        try:

            payload = self.admin_query.create_resource(self.session, admin)

            if payload.http_code != 200:
                raise Exception("There was a problem processing the payload")

        except Exception as e:
            logger.error(f'An unexpected error occurred: {e} Check if admin was successfully added')
    
    # Calls get resource method in admin query class to retrieve admin by login id
    def get_admin_from_login_id (self, login_id: int) -> Dict:

        try:
        
            admin = self.admin_query.get_resource_by_id(self.session, login_id)

            if admin == None:
                raise Exception(f'Could not find admin with login id {login_id}')
        
            return admin 

        except Exception as e:
            logger.warning(f'{e}')
            return None

            
