import sqlalchemy
from loguru import logger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from main.utilities.load_env_file import Environment

def get_connection () -> sqlalchemy.engine.base.Engine:
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
    return pool

try:

    Base = automap_base()
    engine = get_connection()
    local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

except Exception as e:
    logger.error(f'There was an error connecting to the development database: {e}')