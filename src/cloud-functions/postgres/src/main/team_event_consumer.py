from main.database.query_classes.team_query import ConstructTeamQuery
from main.database.session import local_session

from main.schemas.schemas_team import TeamBase
from main.schemas.schemas_error import Error

from main.utilities.create_obj_from_schema import ObjectBuilder

from loguru import logger

class PostgresTeamEventConsumer:

    session = local_session()

    @classmethod
    def process_add_team_request (cls, team: TeamBase) -> Error:

        logger.debug("Attempting to add new team to database")

        team_query_constructor = ConstructTeamQuery(dk_session=cls.session)
        
        # Going to want to send this to some sort of status topic in the future
        # For now just catching it will do
        status_payload = team_query_constructor.insert_into_team_table(team=team)

        if status_payload.status_code == 200:
            logger.info('Successfully inserted new team to database')
        
        cls.session.close()

        return ObjectBuilder().convert_status_to_error(status=status_payload)
    

    def process_delete_team_request (cls, team_id: int) -> Error:

        logger.debug('Attempting to delete team from database')

        team_query_constructor = ConstructTeamQuery(dk_session=cls.session)

        status_payload = team_query_constructor.delete_team_from_table(team_id=team_id)

        if status_payload.status_code == 200:
            logger.info("Successfully deleted team from database")
        
        # Close Session
        cls.session.close()

        return ObjectBuilder().convert_status_to_error(status=status_payload)
