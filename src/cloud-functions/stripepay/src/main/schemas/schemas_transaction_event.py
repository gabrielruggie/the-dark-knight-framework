from pydantic import BaseModel
from typing import Optional

class TransactionBase (BaseModel): 
    first_name: Optional[str]
    last_name: Optional[str]
    amount: Optional[int]
    transaction_date: Optional[str]
    transaction_time: Optional[str]

class TransactionEvent (TransactionBase):
    stripe_payer_id: Optional[str]
    physical: Optional[int]
    verified: Optional[int]
    archived: Optional[int]

class TransactionDatabase (TransactionEvent):
    id: Optional[int]

class CanvasTransaction (TransactionBase):
    id: Optional[int]