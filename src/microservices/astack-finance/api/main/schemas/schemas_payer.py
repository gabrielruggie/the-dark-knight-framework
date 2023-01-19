from typing import Optional
from pydantic import BaseModel

'''
User will fill out a form at the route: /begin-transaction.
They will give this information which we will use to validate them on the backend
'''
class StripePayer (BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    amount: Optional[int]

'''
Event to be sent to dk.payment.pending topic
'''
class StripePayerEvent (StripePayer):
    event_type: Optional[str]
    date: Optional[str]
    status: Optional[str]
    payer_id: Optional[str]
