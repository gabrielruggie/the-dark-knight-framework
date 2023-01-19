from loguru import logger

from main.utilities.serializer import ByteConverter
from main.utilities.create_obj_from_schema import ObjectBuilder
from main.utilities.resource_loader import ResourceLoader

from main.transaction_consumer import GoogleTransactionEventConsumer

from main.schemas.schemas_error import Error

from main.config.cache_connection import connection

'''
Entry point for the Google Transaction Event Consumer
'''
def process (event, context):

    logger.info(f'Received new event from dk.events.sheet-scraper-v1: {event} with context: {context}')

    payload = ByteConverter().deserialize_to_dict(encoded_bytes=event['data'])
    logger.info(f'DK deserialized event to: {payload}')

    resource_loader = ResourceLoader()
    resource_loader.load_service_file()

    event_source = payload['source']
    event_trigger = payload['trigger']

    if event_source in resource_loader.REGISTERED_SERVICES:

        payload_data = payload['data']
        payload_data_struct = eval(payload_data)

        transaction = ObjectBuilder().build_transaction_event(data=payload_data_struct)
        event_handler = GoogleTransactionEventConsumer()

        status = event_handler.process(transaction=transaction, metadata={'service': event_source, 'admin': event_trigger})

        # Checking if admin id is attached because strip doesn't send one
        if len(event_trigger) > 0 and status.is_cached == 1:
            __cache_error(admin_id=event_trigger, service=event_source, error=status)  
    else:
        logger.warning(f'Unrecognized service sender: {event_source}')

'''
Caches error attached to admin sender
'''
def __cache_error (admin_id: str, service: str, error: Error) -> None:

    error.admin_id = admin_id
    error.service = service
    error.cache_key = f'{admin_id}.{service}.status'

    key = error.cache_key

    status_bytes = ByteConverter().serialize_to_bytes(data=dict(error))
    connection.set(key, status_bytes)
    logger.info('Cached new error created in google sheet scraper cloud function.')
    
