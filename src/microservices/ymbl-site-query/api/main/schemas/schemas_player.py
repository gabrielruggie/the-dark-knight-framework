from pydantic import BaseModel
from typing import Optional

# Get rid of email, position, and grade
# Set player number to 0 off rip
class PlayerBase (BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    player_number: Optional[int]
class PlayerDatabase (PlayerBase):
    id: Optional[str]
    team_id: Optional[int]
    team_church: Optional[str]
    team_cap_name: Optional[str]
    team_level: Optional[int]
    tot_points: Optional[int]
    tot_assists: Optional[int]
    tot_rebounds: Optional[int]
    tot_steals: Optional[int]
    tot_blocks: Optional[int]
    games_played: Optional[int]

class PlayerStats (PlayerBase):
    id: Optional[str]
    team_church: Optional[str]
    team_cap_name: Optional[str]
    team_level: Optional[int]
    team_id: Optional[int]
    tot_points: Optional[int]
    tot_assists: Optional[int]
    tot_rebounds: Optional[int]
    tot_steals: Optional[int]
    tot_blocks: Optional[int]
    games_played: Optional[int]
    
# # # # # # # # # # # # # # #

class PlayerSheets (PlayerBase):
    is_team_captain: Optional[int]
    team_church: Optional[str]
    team_cap_name: Optional[str]
    team_level: Optional[int]



class PlayerWeb (BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    player_number: Optional[int]
    position: Optional[str]
    team_id: Optional[int]
    team_church: Optional[str]
    team_cap_name: Optional[str]
    team_level: Optional[int]
    ppg: Optional[str]
    apg: Optional[str]
    rpg: Optional[str]
    spg: Optional[str]
    bpg: Optional[str]
    games_played: Optional[int]
