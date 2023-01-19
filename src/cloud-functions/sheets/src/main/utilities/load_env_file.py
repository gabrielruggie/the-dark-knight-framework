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

    TEST_YMBL_PRICE = os.getenv('TEST_YMBL_PRICE', 100)

    POSTGRES_EVENTS_TOPIC = os.getenv('POSTGRES_EVENTS_TOPIC')