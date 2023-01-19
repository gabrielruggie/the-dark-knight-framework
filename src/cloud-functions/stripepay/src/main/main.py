from loguru import logger

from main.utilities.serializer import ByteConverter
from main.utilities.load_env_file import Environment
from main.utilities.resource_loader import ResourceLoader

from main.pending_payment_consumer import StripePendingPaymentConsumer
from main.completed_payment_consumer import StripeCompletedPaymentConsumer

'''
Entry point for website stripe payment event handler
'''
def process (event, context):

    logger.info(f'Received new event from {Environment.PAYMENT_TOPIC}: {event} with context: {context}')

    payload = ByteConverter().deserialize_to_dict(encoded_bytes=event['data'])
    logger.info(f'DK deserialized event to: {payload}')

    resource_loader = ResourceLoader()
    resource_loader.load_service_file()

    event_source = payload['source']

    # First verify that source is a valid source that should have access to this topic
    if event_source in resource_loader.REGISTERED_SERVICES:

        payload_data = payload['data']
        payload_data_struct = eval(payload_data)

        # Use match here for faster indexing
        match payload_data_struct['status']:

            case 'pending':
                StripePendingPaymentConsumer().process(event=payload_data_struct)

            case 'completed':
                StripeCompletedPaymentConsumer().process(event=payload_data_struct)    

            case _:
                status = payload_data_struct['status']
                logger.warning(f'Received event when unknown status: {status}. Ignoring...')
    
    else:
        logger.warning(f'Received event from unknown sender: {event_source}. Ignoring...')

