from dotenv import load_dotenv
import os

from loguru import logger

try:
    load_dotenv()
except Exception as e:
    logger.warning(f'There was an error loading in the environment variables for this website service')

class Environment:

    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD') 

    POSTGRES_USER = os.getenv('POSTGRES_USER') 

    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

    POSTGRES_DB = os.getenv('POSTGRES_DB') 

    POSTGRES_HOST = os.getenv('POSTGRES_HOST')

    POSTGRES_UXPATH = os.getenv('POSTGRES_UXPATH')

    IS_LOCAL_CONTAINER = os.getenv('IS_LOCAL_CONTAINER')