from pydantic import BaseModel
from typing import Optional

class Applicant (BaseModel):
    id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    year: Optional[str]
    position: Optional[str]
    number: Optional[int]
    church: Optional[str]
    team_level: Optional[str]
    # Boolean thats a string in the sheet
    team_captain_last_name: Optional[str]
    payer_first_name: Optional[str]
    payer_last_name: Optional[str]
    amount_owed: Optional[int]

