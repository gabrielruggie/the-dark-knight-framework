from redis import StrictRedis
from main.utilities.load_env_file import Environment

# Connect to Redis Cache Hosted By Redis Labs
# If db is deleted due to inactivity, remove port from end of link of new db
connection = StrictRedis(
    host='redis-13238.c280.us-central1-2.gce.cloud.redislabs.com',
    port=13238,
    password=Environment.REDIS_PASSWORD,
    decode_responses=True,
    ssl=False
)