import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from main.utilities.load_env_file import Environment

from loguru import logger

# Logic to tell container if we are testing locally or in the cloud
def get_connection () -> sqlalchemy.engine.base.Engine:

    if int(Environment.IS_LOCAL_CONTAINER) == 1:
        # Retrieve environment variables from path specified
        USER = Environment.POSTGRES_USER
        PASSWORD = Environment.POSTGRES_PASSWORD
        DATABASE = Environment.POSTGRES_DB
        HOST = Environment.POSTGRES_HOST

        pool = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}')
        logger.info(f'Engine Created For ASTACK Finance: {pool}')
        return pool

    else:
        
        db_user = Environment.POSTGRES_USER
        db_pass = Environment.POSTGRES_PASSWORD
        db_name = Environment.POSTGRES_DB
        unix_socket_path = Environment.POSTGRES_UXPATH

        pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                database=db_name,
                query={"unix_sock": "{}/.s.PGSQL.5432".format(unix_socket_path)},
            ),
        )
        logger.info(f'Engine Created For ASTACK Finance: {pool}')
        return pool

local_session = None
engine = None
Base = None
try:
    
    Base = automap_base()
    engine = get_connection()
    local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

except Exception as e:
    logger.warning(f'An error occurred while attemption to connection to database: {e}')