from typing import Dict

from main.config.cache_connection import connection

from main.utilities.serializer import ByteConverter

from loguru import logger

'''
This consumer has to take a pending payment and add it to a cache
'''
class StripePendingPaymentConsumer:

    @classmethod
    def process (cls, event: Dict):
        
        try:

            payer_id = event['payer_id']
            event_base64 = ByteConverter().serialize_to_bytes(data=event)

            connection.set(payer_id, event_base64)  

            logger.info(f'Successfully cached pending payment from payer: {payer_id}')

        except Exception as e:
            logger.error(f'Unexpected error occurred. Check connection to Redis caches: {e}')