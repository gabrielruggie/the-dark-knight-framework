from typing import Optional, List
from pydantic import BaseModel

class TeamBase (BaseModel):
    church: Optional[str]
    school_level: Optional[int]
    cap_last_name: Optional[str]

class TeamDatabase (TeamBase):
    id: Optional[int]
    team_name: Optional[str]

class TeamStats (BaseModel):
    team_name: Optional[str]
    roster: Optional[List]

# # # # # # # # # # # # # # #

class TeamCanvas (BaseModel):
    id: Optional[int]

class TeamWebsite (TeamBase):
    id: Optional[int]       # For team logo alignment
    wins: Optional[str]
    losses: Optional[str]

