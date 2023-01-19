from fastapi import APIRouter, Depends, responses
from fastapi.security import OAuth2PasswordRequestForm

from main.schemas.schemas_response import Response
from main.schemas.schemas_admin import AdminDarkKnightBase

from main.config.cache_connection import connection

from main.utilities.load_env_file import Environment
from main.utilities.serializer import ByteConverter
from main.utilities.create_obj_from_schema import ObjectBuilder
from main.utilities.verify_user_credentials import VerifyUserFactory

from main.routes.security.token import TokenFactory

from main.database.generate_session import generate_session_instance
from sqlalchemy.orm import Session
from loguru import logger
from datetime import timedelta
import base64


# Retrieve environment variables from path specified
TOKEN_EXP_TIME = int(Environment.TOKEN_EXPIRE_TIME_MINUTES)

token = APIRouter()

'''
PLAN: Concatenate the login_id to the admin's password and convert the concatenated
string to base64 on the frontend side, then send it in the password field to the backend

Here, we need to decode it from base64. Extract the login_id and password and verify
both parts, then create a token with parts `sub`, `username`, and `admin_level`
'''

@token.post("/token")
async def create_token_off_login (admin: OAuth2PasswordRequestForm = Depends(),dk_session: Session = Depends(generate_session_instance)):

    username = admin.username
    password_key = admin.password

    if len(username) == 0 and len(password_key) == 0:
        logger.debug("Could not parse user input")
        response = Response(http_code=500, error_code=330, msg='One or more fields was left empty!')
        return responses.JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=response)))

    logger.info(f'Received username {username} and password-key {password_key}')

    password_key_bytes = base64.b64decode(password_key)
    password_key_obj = password_key_bytes.decode("utf-8")
    password_loginid = eval(password_key_obj)

    password = password_loginid["password"]
    login_id = int(password_loginid["login_id"])

    logger.debug(f'Decoded password-key parts as password: {password} and login_id: {login_id}')
    logger.debug(f'Verifing username, password and login id with DK')

    user_factory = VerifyUserFactory()
    payload = user_factory.verify_admin_and_return(login_id=login_id, password=password, username=username, session=dk_session)

    if payload.http_code != 200:
        logger.debug(f'{payload.msg}')
        return responses.JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=payload)))

    user_data = payload.msg.split(',')

    verified_loginid = user_data[0].strip()
    verified_username = user_data[1].strip()
    verified_rightlevel = user_data[2].strip()

    logger.info(f'Received user with login_id: {verified_loginid}, username: {verified_username}, right_level: {verified_rightlevel}')

    # Defines token expiration timer
    token_expiration_time = timedelta(minutes=TOKEN_EXP_TIME)

    # Admin Token Content
    content = {
        "login_id": int(verified_loginid),
        "username": verified_username,
        "right_level": int(verified_rightlevel)
    }

    # Creates access token
    token = TokenFactory.create_token(data=content, expires=token_expiration_time)
    # Cache token
    admin_data = ByteConverter().serialize_to_bytes(data=content)
    connection.set(login_id, admin_data)
    logger.info(f'Cached admin with token: {token}')

    return {"access_token": token, "token_type": "bearer"}

'''
Route to verify astack users accessing the user interface
'''
@token.get("/verify-astack-admin-token")
async def verify_user (admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token)):
    return responses.JSONResponse(content=admin)

