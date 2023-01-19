from typing import Optional
from pydantic import BaseModel

class TeamBase (BaseModel):
    church: Optional[str]
    school_level: Optional[int]
    cap_last_name: Optional[str]

class TeamDatabase (TeamBase):
    id: Optional[int]
    wins: Optional[int]
    losses: Optional[int]
    total_pts: Optional[int]
    pts_allowed: Optional[int]

class TeamUpdate (BaseModel):
    wins: Optional[int]
    losses: Optional[int]
    total_pts: Optional[int]
    pts_allowed: Optional[int]

class TeamCanvas (BaseModel):
    id: Optional[int]

class TeamWebsite (BaseModel):
    id: Optional[int]       # For team logo alignment
    wins: Optional[str]
    losses: Optional[str]