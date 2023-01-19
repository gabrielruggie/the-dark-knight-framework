from typing import Dict
from loguru import logger 
from main.config.cache_connection import connection
from main.utilities.load_env_file import Environment

from google.cloud import pubsub_v1
import json

'''
General event publisher that sends an event as a dictionary to our redis streaming service
'''
class EventPublisher:

    def __init__ (self, topic_name: str, event: Dict):
        self.session = connection
        self.topic_name = topic_name 
        self.event = event
        self.project = Environment.GOOGLE_CLOUD_PROJECT

    '''
    Attempts to send event to streaming service. Sends payload back with results.
    '''
    def publish (self) -> None:

        try: 

            client = pubsub_v1.PublisherClient()
            topic_path = client.topic_path(self.project, self.topic_name)

            data = json.dumps(self.event)

            future = client.publish(topic_path, data.encode('ascii'))

            logger.info(f'Published new event: {data} to topic: {topic_path}')

        except Exception as e:
            logger.error(f'Received unexpected error while trying to publish new event: {e}')
            raise Exception
            