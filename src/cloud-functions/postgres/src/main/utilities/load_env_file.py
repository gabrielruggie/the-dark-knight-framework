from dotenv import load_dotenv
import os

try:
    load_dotenv()
except Exception:
    pass

class Environment:
    
    GOOGLE_EVENTS_TOPIC = os.getenv('GOOGLE_EVENTS_TOPIC') 

    GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT')

    PAYMENT_TOPIC = os.getenv('PAYMENTS_TOPIC') 

    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD') 

    POSTGRES_EVENTS_TOPIC = os.getenv('POSTGRES_EVENTS_TOPIC')

    POSTGRES_USER = os.getenv('POSTGRES_USER') 

    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

    POSTGRES_DB = os.getenv('POSTGRES_DB') 

    POSTGRES_UXPATH = os.getenv('POSTGRES_UXPATH')