from main.schemas.schemas_response import Response
from main.utilities.load_env_file import Environment
from main.config.cache_connection import connection

from google.cloud import pubsub_v1

from loguru import logger 
from typing import Dict
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
    def publish (self) -> Response:

        try: 

            client = pubsub_v1.PublisherClient()
            topic_path = client.topic_path(self.project, self.topic_name)

            data = json.dumps(self.event)

            future = client.publish(topic_path, data.encode('ascii'))

            logger.info(f'Published new event: {data} to topic: {topic_path}')
        
            return Response(http_code=200, error_code=0, msg='')

        except Exception as e:
            logger.error(f'Received unexpected error while trying to publish new event: {e}')
            return Response(http_code=500, error_code=350, msg='An unexpected error occurred while processing your request. Please inform your supervisor of this error.')
            