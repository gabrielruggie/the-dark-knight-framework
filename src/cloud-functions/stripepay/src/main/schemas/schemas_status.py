from typing import Optional
from pydantic import BaseModel

'''
Status Object to be cached by all cloud functions in order for frontend to retrieve them
'''
class Status (BaseModel):
    schema_version: Optional[str]
    http_code: Optional[int]
    msg: Optional[str]
    admin_id: Optional[str]
    log_type: Optional[str]
    is_cached: Optional[int]
    sender: Optional[str]
    cache_key: Optional[str]

