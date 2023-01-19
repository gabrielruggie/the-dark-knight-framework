from main.database.query_classes.transaction_query import ConstructTransactionQuery
from main.database.session import local_session

from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_transaction_event import TransactionEvent
from main.schemas.schemas_error import Error
from main.schemas.schemas_status import Status

from loguru import logger

class PostgresTransactionEventConsumer:


    session = local_session()

    @classmethod
    def process_add_transaction_request (cls, transaction: TransactionEvent) -> Error:

        transaction_query_constructor = ConstructTransactionQuery(dk_session=cls.session)
        
        # Going to want to send this to some sort of status topic in the future
        # For now just catching it will do
        status_payload = transaction_query_constructor.insert_transaction_to_table(transaction=transaction)

        if status_payload.status_code == 200:
            logger.info("Successfully inserted transaction to database")
        
        # Close Session 
        cls.session.close()

        return ObjectBuilder().convert_status_to_error(status=status_payload)
    

    @classmethod
    def process_delete_transaction_request (cls, transaction_id: int) -> Error:

        transaction_query_constructor = ConstructTransactionQuery(dk_session=cls.session)

        status_payload = transaction_query_constructor.delete_transaction_from_table(transaction_id=transaction_id)

        if status_payload.status_code == 200:
            logger.info("Successfully removed transaction from database")

        # Close Session 
        cls.session.close()

        return ObjectBuilder().convert_status_to_error(status=status_payload)

        