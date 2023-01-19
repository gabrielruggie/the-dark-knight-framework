from dotenv import load_dotenv
import os

try:
    load_dotenv()
except Exception:
    pass

class Environment:

    API_VERSION = os.getenv('API_VERSION')

    TOKEN_SECRET_KEY = os.getenv('TOKEN_SECRET_KEY', 'dktokentestkey')

    TOKEN_ALGORITM = os.getenv('TOKEN_ALGORITM', 'HS256')

    DK_ADMIN_TOKEN_URL = os.getenv('DK_ADMIN_TOKEN_URL')

    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD') 

    POSTGRES_USER = os.getenv('POSTGRES_USER') 

    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

    POSTGRES_DB = os.getenv('POSTGRES_DB') 

    POSTGRES_HOST = os.getenv('POSTGRES_HOST')

    POSTGRES_EVENTS_TOPIC = os.getenv('POSTGRES_EVENTS_TOPIC')

    POSTGRES_UXPATH = os.getenv('POSTGRES_UXPATH')

    PAYMENT_TOPIC = os.getenv('PAYMENTS_TOPIC')
    
    GOOGLE_EVENTS_TOPIC = os.getenv('GOOGLE_EVENTS_TOPIC') 

    GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT')

    IS_LOCAL_CONTAINER = os.getenv('IS_LOCAL_CONTAINER')