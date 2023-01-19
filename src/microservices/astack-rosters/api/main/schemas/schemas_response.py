from pydantic import BaseModel
from typing import Optional

'''
Status payload that must be converted to dictionary in order to be returned as a JSON Object
'''
class Response(BaseModel):
    http_code: Optional[int]
    error_code: Optional[int]
    msg: Optional[str]

class ServiceResponse (Response):
    schema_version: Optional[str]
