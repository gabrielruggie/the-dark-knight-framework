from dotenv import load_dotenv
import os

from loguru import logger

try:
    load_dotenv()
except Exception:
    logger.warning('There was an error retrieving the environment variables for this container')

class Environment:

    API_VERSION = os.getenv('API_VERSION')

    TOKEN_EXPIRE_TIME_MINUTES = os.getenv('TOKEN_EXPIRE_TIME_MINUTES', 60)

    TOKEN_SECRET_KEY = os.getenv('TOKEN_SECRET_KEY', 'dktokentestkey')

    TOKEN_ALGORITM = os.getenv('TOKEN_ALGORITM', 'HS256')

    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD') 

    DK_VALIDATION_KEY = os.getenv('DK_VALIDATION_KEY', 'dk-validation-key') 

    POSTGRES_USER = os.getenv('POSTGRES_USER') 

    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

    POSTGRES_DB = os.getenv('POSTGRES_DB') 

    POSTGRES_HOST = os.getenv('POSTGRES_HOST')

    POSTGRES_UXPATH = os.getenv('POSTGRES_UXPATH')

    IS_LOCAL_CONTAINER = os.getenv('IS_LOCAL_CONTAINER')
