from typing import Dict
from datetime import date, datetime
from main.config.base_event import Event
import random

from loguru import logger
import json

class EventBuilder:

    def __init__ (self, data: Dict, data_type: str, data_source: str, topic_published_to: str, publisher_name: str):
        self.data = data
        self.type = data_type
        self.topic = topic_published_to
        self.source = data_source
        self.trigger = publisher_name
        self.today = date.today().strftime("%m/%d/%y")
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.data_content_type = 'application/json'
        self.event_schema_version = '1.0'
    
    def create (self) -> Event:

        try:

            event = Event(
                version=self.event_schema_version,
                type=self.type,
                topic=self.topic,
                source=self.source,
                trigger=self.trigger,
                id=self.__create_id(),
                date=self.today,
                time=self.timestamp,
                data_content_type=self.data_content_type,
                data=json.dumps(self.data)
            )

            return event
        
        except Exception as e:
            logger.error(f'Event builder encountered unexpected error: {e}')
    
    def __create_id (self) -> int:
        return random.randint(100000, 999999)

