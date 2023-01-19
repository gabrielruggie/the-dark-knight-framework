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
    transaction_date: Optional[str]
    transaction_time: Optional[str]

'''
Event to be sent to dk.payment.pending topic
'''
class StripePayerEvent (StripePayer):
    status: Optional[str]
    payer_id: Optional[str]
