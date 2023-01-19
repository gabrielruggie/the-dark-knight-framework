from pydantic import BaseModel
from typing import Optional

'''
Status payload that must be converted to dictionary in order to be returned as a JSON Object
'''
class StatusPayload(BaseModel):
    status: Optional[str]
    message: Optional[str]
