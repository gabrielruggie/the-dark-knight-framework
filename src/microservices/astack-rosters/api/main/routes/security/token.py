from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Dict

from main.config.cache_connection import connection
from main.utilities.load_env_file import Environment
from main.utilities.serializer import ByteConverter
from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_admin import AdminDarkKnightBase

from loguru import logger

'''
JWT Token class that creates and manages an admin's jwt token
'''
class TokenFactory:

    OAuth2Scheme =  OAuth2PasswordBearer(tokenUrl=f'{Environment.DK_ADMIN_TOKEN_URL}')
    TOKEN_ALGORITM = Environment.TOKEN_ALGORITM
    TOKEN_SECRET_KEY = Environment.TOKEN_SECRET_KEY

    # This acts as a dependency. Any webpage that requires a logged in user will depend on this
    # function to authenticate the current user based on the JWT thats alive
    @classmethod
    def get_user_from_token (cls, token: str = Depends(OAuth2Scheme)) -> AdminDarkKnightBase:

        try:
            # Decode the current JWT alive
            payload = jwt.decode(token, key=cls.TOKEN_SECRET_KEY, algorithms=cls.TOKEN_ALGORITM)

            login_id = payload.get("login_id")
            username = payload.get("username")
            right_level = payload.get("right_level")

            # If the JWT does not exist anymore, the user will need to login again
            # Catch this in the method that depended on it
            if login_id == None or username == None or right_level == None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not authorize current user")
            logger.debug("Token contents decoded. Verifing user with DK now...")

        except JWTError as e:
            logger.debug(f'There was a problem verifing the current user. login_id found: {login_id}, username found: {username}, right_level found: {right_level}')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{e}")

        # admin_query_factory = ConstructAdminQuery(dk_session=session)
        # admin = admin_query_factory.get_admin_from_login_id(login_id=login_id)

        # Query cache instead of large database
        admin_data_bytes = connection.get(login_id)

        # If the user attempts to login after deleting their account, throw this
        if admin_data_bytes == None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")
        
        admin_jwt = ByteConverter().deserialize_to_dict(encoded_bytes=admin_data_bytes)

        admin = ObjectBuilder().build_admin_base(data=admin_jwt)

        logger.debug(f'Retrieved admin from cache with data: {admin}. Returning...')
        return admin