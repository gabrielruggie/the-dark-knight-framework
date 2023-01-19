from pydantic import BaseModel
from typing import Dict, Optional

'''
Base Model for all Events in the DK framework.

{
    version: `currently 1.0`
    type: `event type i.e: transaction, player, etc...`
    topic: `topic that received this event`
    source: `origin service or funtion event is coming from`
    trigger: `admin who triggered event`
    id: `random 6 digit number`
    date: `datetime converted to string`
    time: `time converted to string`
    data_content_type: `application/json`
    data_base64: `data field as base64`
    data: `Any schema as a dictionary`
}
'''

class Event(BaseModel):
    version: Optional[str]
    type: Optional[str]
    topic: Optional[str]
    source: Optional[str]
    trigger: Optional[str]
    id: Optional[int]
    date: Optional[str]
    time: Optional[str]
    data_content_type: Optional[str]
    data: Optional[str]


