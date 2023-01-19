from main.database.session import Base, engine
import sqlalchemy
from loguru import logger

connection = False
'''
Attempts to connect to DK, however, catches sqlalchemy error and logs connection error
'''
try:
    
    Base.prepare(autoload_with=engine)
    connection = True

except sqlalchemy.exc.OperationalError as e:
    logger.info("Connection to DK Database could not be made")

'''
Utility class that stores all of tables in DK as Base classses 
'''
class Table:

    # Transaction = Base.classes.transaction if connection == True else None

    Team = Base.classes.team if connection == True else None

    Player = Base.classes.player if connection == True else None

