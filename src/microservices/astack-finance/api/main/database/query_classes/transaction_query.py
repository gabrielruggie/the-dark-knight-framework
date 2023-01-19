from main.database.tables.table import Table
from main.database.query_classes.base_query import BaseQuery

from main.schemas.schemas_transaction_event import TransactionDatabase, CanvasTransaction

from loguru import logger
from sqlalchemy.orm import Session

class TransactionQuery(BaseQuery[Table.Transaction, TransactionDatabase, CanvasTransaction]):
    ...

class ConstructTransactionQuery:

    def __init__(self, dk_session: Session):
        self.session = dk_session
        self.transaction_query = TransactionQuery(Table.Transaction, tablename='transaction')
    
    def retrieve_all_transactions (self):

        try:

            return self.transaction_query.get_all_resources(dk_session=self.session)
        
        except Exception as e:
            logger.error(f'{e}')

