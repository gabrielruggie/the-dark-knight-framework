from pydantic import BaseModel
from typing import Optional

class Applicant (BaseModel):
    id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    number: Optional[int]
    age: Optional[int]
    email: Optional[str]
    year: Optional[int]
    team_name: Optional[str]
    team_id: Optional[str]
    
    # Boolean thats a string in the sheet
    team_cap: Optional[str]
    amount_owed: Optional[int]
    venmo_username: Optional[str]

