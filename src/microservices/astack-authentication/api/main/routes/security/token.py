from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from datetime import timedelta
from typing import Optional
from loguru import logger

from main.config.cache_connection import connection

from main.utilities.load_env_file import Environment
from main.utilities.serializer import ByteConverter
from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_admin import AdminDarkKnightBase


'''
JWT Token class that creates and manages an admin's jwt token
'''
class TokenFactory:

    OAuth2Scheme =  OAuth2PasswordBearer(tokenUrl=f'/admin-stack/{Environment.API_VERSION}/oauth/authenticator/token')
    TOKEN_EXP_TIME = Environment.TOKEN_EXPIRE_TIME_MINUTES
    TOKEN_ALGORITM = Environment.TOKEN_ALGORITM
    TOKEN_SECRET_KEY = Environment.TOKEN_SECRET_KEY

    # Creates a JWT access token that expires in case it is intercepted
    @classmethod
    def create_token (cls, data: dict(), expires: Optional[timedelta] = None) -> str:
        logger.debug("Received token content. Creating token...")
        user_info = data.copy()
        # If expires is specified, add it to token expiration time
        if expires:
            expiration_time = datetime.utcnow() + expires
        else:
            # Add time if no expiration duration is specified
            expiration_time = datetime.utcnow() + timedelta(minutes=int(cls.TOKEN_EXP_TIME))

        # Add expiration timer to JWT schema
        user_info.update({"exp": expiration_time})
        # Create JWT token out of user data and expiration information
        security_token = jwt.encode(user_info, key=cls.TOKEN_SECRET_KEY, algorithm=cls.TOKEN_ALGORITM)

        return security_token
    
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
            logger.error(f'{e}')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{e}")

        # Query cache instead of large database
        admin_data_bytes = connection.get(login_id)

        # If the user attempts to login after deleting their account, throw this
        if admin_data_bytes == None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")
        
        admin_jwt = ByteConverter().deserialize_to_dict(encoded_bytes=admin_data_bytes)

        # admin = ObjectBuilder().build_admin_base(data=admin_jwt)

        logger.debug(f'Retrieved admin from cache with data: {admin_jwt}. Returning...')
        
        # Testing for now, don't want to convert to object if we don't need to 
        return admin_jwt