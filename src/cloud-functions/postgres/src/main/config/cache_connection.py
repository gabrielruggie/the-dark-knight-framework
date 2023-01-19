from redis import StrictRedis, Redis
from utilities.load_env_file import Environment

# Connect to Redis Cache Hosted By Redis Labs
connection = StrictRedis(
    host='redis-14339.c280.us-central1-2.gce.cloud.redislabs.com',
    port=14339,
    password=Environment.REDIS_PASSWORD,
    decode_responses=True,
    ssl=False
)