from fastapi import APIRouter, Depends, responses
from loguru import logger

from main.routes.security.token import TokenFactory

from main.schemas.schemas_admin import AdminDarkKnightBase
from main.schemas.schemas_transaction_event import TransactionBase, TransactionEvent

from main.config.event_publisher import EventPublisher
from main.config.event_builder import EventBuilder

from main.database.generate_session import generate_session_instance
from main.database.query_classes.transaction_query import ConstructTransactionQuery

from main.utilities.load_env_file import Environment
from main.utilities.create_obj_from_schema import ObjectBuilder

from sqlalchemy.orm import Session

finance = APIRouter()

'''
Finanace canvas page that loads all transactions from DK
'''
@finance.get("/canvas")
async def canvas_page (
    admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token),
    session: Session = Depends(generate_session_instance)
    ):
    # Gonna call database here eventually
    logger.info(f'Connected to database with session instance: {session}')

    transaction_query_constructor = ConstructTransactionQuery(dk_session=session)
    data = transaction_query_constructor.retrieve_all_transactions()

    logger.info(f'Retrieved transactions: {data} from database')

    return responses.JSONResponse(content=data, status_code=200)


'''
Allows users to add a new transaction in case some players/parents did not pay with venmo
'''
@finance.post("/add-transaction")
async def add_new_transaction (
    transaction: TransactionBase, 
    admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token)
    ):
    
    logger.info(f'Received transaction with data: {dict(transaction)}')
    transaction_data = TransactionEvent(
        first_name=transaction.first_name,
        last_name=transaction.last_name,
        amount=transaction.amount,
        # Note: Have frontend fill these in for us :)
        transaction_date=transaction.transaction_date,
        transaction_time=transaction.transaction_time,
        stripe_payer_id="",
        physical=1,
        verified=0,
        archived=0
    )

    event_builder = EventBuilder(
        data=dict(transaction_data),
        data_type='transaction',
        topic_published_to=Environment.GOOGLE_EVENTS_TOPIC,
        data_source='astackfinance',
        publisher_name=admin.username
    )

    transaction_event = event_builder.create()
    publisher = EventPublisher(Environment.GOOGLE_EVENTS_TOPIC, dict(transaction_event))
    resulting_payload = publisher.publish()

    return responses.JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=resulting_payload)))

'''
Allows users to delete transactions in case of refunds or duplicate recordings
'''
@finance.delete("/delete-transaction/{transaction_id}")
async def remove_transaction_from_tracker (
    transaction_id: int,
    admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token)
    ):

    delete_transaction = {'transaction_id': transaction_id}

    event_builder = EventBuilder(
        data=delete_transaction,
        data_type='transaction.delete',
        topic_published_to=Environment.POSTGRES_EVENTS_TOPIC,
        data_source='astackfinance',
        publisher_name=admin.username
    )

    delete_transaction_event = event_builder.create()

    publisher = EventPublisher(topic_name=Environment.POSTGRES_EVENTS_TOPIC, event=dict(delete_transaction_event))
    resulting_payload = publisher.publish()

    return responses.JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=resulting_payload)))
