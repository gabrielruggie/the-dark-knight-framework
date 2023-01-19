from main.database.query_classes.player_query import ConstructPlayerQuery
from main.database.session import local_session

from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_player import PlayerSheets
from main.schemas.schemas_error import Error

from loguru import logger

'''
Process an event for the player table in main database
'''
class PostgresPlayerEventConsumer:

    session = local_session()

    '''
    Processes new player requests
    '''
    @classmethod
    def process_add_player_request (cls, player: PlayerSheets) -> Error:

        logger.info("Attempting to add new player to database")

        player_query_constructor = ConstructPlayerQuery(dk_session=cls.session)

        status_payload = player_query_constructor.insert_into_player_table(player=player)

        if status_payload.status_code == 200:
            logger.info("Successfully inserted player to database")

        try:

            # Close Session 
            cls.session.close()
        
        except Exception as e:
            logger.warning(f'There was an error while closing the query session for the player event consumer; {e}')

        return ObjectBuilder().convert_status_to_error(status=status_payload)

    '''
    Processes deleting existing player requests
    '''
    def process_delete_player_request (cls, player_id: str) -> Error:

        logger.debug('Attempting to delete player from database')

        player_query_constructor = ConstructPlayerQuery(dk_session=cls.session)

        status_payload = player_query_constructor.delete_from_player_table(player_id=player_id)

        if status_payload.status_code == 200:
            logger.info("Successfully deleted team from database")
        
        try:

            # Close Session 
            cls.session.close()
        
        except Exception as e:
            logger.warning(f'There was an error while closing the query session for the player event consumer; {e}')

        return ObjectBuilder().convert_status_to_error(status=status_payload)