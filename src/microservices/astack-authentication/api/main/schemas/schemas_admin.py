from pydantic import BaseModel
from typing import Optional

'''
Basic admin fields. Acts as payload from login or registration
'''
class AdminDarkKnightBase(BaseModel):
    username: Optional[str]
    astack_right_level: Optional[int]

'''
Created when a new admin completes a registration form
'''
class NewAdminDarkKnight(AdminDarkKnightBase):
    login_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    confirm_password: Optional[str]
    position: Optional[str]

'''
Update admin schema
Admins can only update their email, username, position and right level
Id is here to query them in DK
'''
class UpdateAdminDarkKnight(AdminDarkKnightBase):
    id: Optional[str]
    position: Optional[str]
    email: Optional[str]

'''
Combination of NewAdminDarkKnight and AdminDarkKnightBase
'''
class AdminDarkKnightDatabase(AdminDarkKnightBase):
    id: Optional[str]
    login_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    hashed_password: Optional[str]
    position: Optional[str]

    class Config:
        orm_mode = True