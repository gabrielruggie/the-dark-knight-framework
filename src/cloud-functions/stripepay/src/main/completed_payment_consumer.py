from main.config.cache_connection import connection
from main.config.event_publisher import EventPublisher
from main.config.event_builder import EventBuilder

from main.utilities.load_env_file import Environment
from main.utilities.serializer import ByteConverter
from main.utilities.create_obj_from_schema import ObjectBuilder

from loguru import logger
from typing import Dict

'''
Receives a completed payment event and create a new transaction event to send to the
Google Transaction Event Consumer
'''
class StripeCompletedPaymentConsumer:
    
    @classmethod
    def process (cls, event: Dict):
        
        try:

            payer_id = event['payer_id']

            encoded_payer_data = connection.get(payer_id)
            logger.debug(f'Found payer data connected to payer_id: {payer_id}')

            connection.delete(payer_id)

            payer = ByteConverter().deserialize_to_dict(encoded_bytes=encoded_payer_data)

            stripe_payer = ObjectBuilder().build_payment_event(data=payer)
            stripe_transaction = ObjectBuilder().convert_stripe_event_to_transaction(stripe_event=stripe_payer)

            event_builder = EventBuilder(
                data=dict(stripe_transaction),
                data_type='transaction',
                data_source='webpayment',   # May want to change this to cf.stripe
                topic_published_to=Environment.GOOGLE_EVENTS_TOPIC,
                publisher_name=''           # Admin did not make this request
            )

            stripe_transaction_event = event_builder.create()

            publisher = EventPublisher(topic_name=Environment.GOOGLE_EVENTS_TOPIC, event=dict(stripe_transaction_event))
            publisher.publish()
            logger.debug(f'Published new event to topic: {Environment.GOOGLE_EVENTS_TOPIC}')

        except Exception as e:
            logger.error(f'An unexpected error occurred. Check connection to cache then check deserilization: {e}')
