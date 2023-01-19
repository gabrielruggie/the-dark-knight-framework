from main.database.session import Base, engine
from loguru import logger

connection = False
'''
Attempts to connect to DK, however, catches sqlalchemy error and logs connection error
'''
try:
    
    Base.prepare(autoload_with=engine)
    connection = True

except Exception as e:
    logger.info(f'Connection to DK Database could not be made. Error: {e}')

'''
Utility class that stores all of tables in DK as Base classses 
'''
class Table:

    Admin = Base.classes.admin if connection == True else None

    Transaction = Base.classes.transaction if connection == True else None
