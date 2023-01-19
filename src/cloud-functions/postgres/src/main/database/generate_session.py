from typing import Generator 
from main.database.session import local_session

'''
Returns a session instance that has a direct connection to DK
'''
def generate_session_instance () -> Generator:
    dk_instance = local_session()

    try:
        yield dk_instance
    finally:
        dk_instance.close()
