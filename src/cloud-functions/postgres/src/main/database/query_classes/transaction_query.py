from typing import Dict

from main.database.query_classes.base_query import BaseQuery, ConstructBaseQuery
from main.database.tables.table import Table
from main.utilities.create_obj_from_schema import ObjectBuilder
from main.schemas.schemas_transaction_event import TransactionDatabase, CanvasTransaction, TransactionEvent
from main.schemas.schemas_status import Status

from loguru import logger
from sqlalchemy.orm import Session

'''
Transaction table specific query class
'''
class TransactionQuery(BaseQuery[Table.Transaction, TransactionDatabase, CanvasTransaction]):

    def get_last_resource_appended (self, dk_session: Session) -> Dict:

        try:

            last_row_data = dk_session.query(self.model).order_by(self.model.id.desc()).first()
            
            if last_row_data == None:
                logger.debug("Could not find any recorded records in Transaction Check. Check that it exists")
                return None

            logger.info(f'Retrieved last row with data: {last_row_data}')
            return self.convert_row_data_to_dict(row=last_row_data)

        except Exception as e:
            logger.error(f'Received error while querying database: {e}')
            raise TransactionQueryException(http_code=500, message='An error occurred while querying the database. Please inform your supervisor of this error. Error Code: 200')

'''
Constructor for transaction table specific query class
'''
class ConstructTransactionQuery(ConstructBaseQuery):

    def __init__(self, dk_session: Session):
        self.session = dk_session
        self.transaction_query = TransactionQuery(Table.Transaction, tablename='transaction')
    
    # Attempts to add a new transaction to database
    # Returns a status payload with result code
    def insert_transaction_to_table (self, transaction: TransactionEvent) -> Status:

        try:

            last_transaction = self.transaction_query.get_last_resource_appended(dk_session=self.session)
            
            next_transaction_id = 0
            if last_transaction != None:
                last_transaction_id = last_transaction["id"]
                next_transaction_id  = int(last_transaction_id) + 1

            transaction_db = ObjectBuilder().convert_transaction_to_database_type(transaction=transaction, next_id=next_transaction_id)

            self.transaction_query.create_resource(dk_session=self.session, resource=transaction_db)

            return Status(status_code=200, message='Successful database insertion')
        
        except TransactionQueryException as t:
            return Status(status_code=t.http_code, message=t.message)

        except Exception as e:
            logger.error(f'Received an unexpected error: {e}')
            return Status(status_code=500, message='An unexpected error occurred while processing your request. Please inform your supervisor of this error. Error Code: 210')
    
    '''
    Attempts to add a new transaction to database
    Returns a status payload with result code
    '''
    def delete_transaction_from_table (self, transaction_id: int) -> Status:

        try:

            transaction_data = self.transaction_query.get_resource_by_id(dk_session=self.session, id=transaction_id)

            if transaction_data == None:
                raise TransactionQueryException(http_code=400, message=f'Transaction with id: {transaction_id} does not exist!')
            
            self.transaction_query.delete_resource_by_id(dk_session=self.session, id=transaction_id)

            return Status(status_code=200, message='Successful database deletion')
        
        except TransactionQueryException as t:
            return Status(status_code=t.http_code, message=t.message)

        except Exception as e:
            logger.error(f'Received an unexpected error: {e}. Check connection to database')
            return Status(status_code=500, message='An unexpected error occurred while querying the database. Please inform your supervisor of this error. Error Code: 220')


class TransactionQueryException (Exception):

    def __init__ (self, http_code: int, message: str):
        self.http_code = http_code
        self.message = message
