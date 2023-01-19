from main.database.tables.table import Table
from main.database.query_classes.base_query import BaseQuery
from main.database.query_classes.team_query import TeamQuery
from main.schemas.schemas_player import PlayerSheets, PlayerDatabase
from main.schemas.schemas_status import Status
from main.utilities.team_id_generator import TeamIdGenerator
from main.utilities.create_obj_from_schema import ObjectBuilder

from loguru import logger
from sqlalchemy.orm import Session

class PlayerQuery (BaseQuery[Table.Player, PlayerDatabase, PlayerDatabase]):
    ...

class ConstructPlayerQuery ():
    
    def __init__ (self, dk_session: Session):
        self.session = dk_session
        self.team_query = TeamQuery(model=Table.Team, tablename='team')
        self.player_query = PlayerQuery(model=Table.Player, tablename='player')
    
    '''
    Attempts to add a new team to the database
    Returns a status payload with result code
    '''
    def insert_into_player_table (self, player: PlayerSheets) -> Status:

        try:

            id_generator = TeamIdGenerator(church=player.team_church, school_level=player.team_level, name=player.team_cap_name)
            team_id = id_generator.generate()

            # Determine if team already exists:
            retrieved = self.team_query.get_resource_by_id(dk_session=self.session, id=team_id)

            if retrieved == None:
                raise PlayerQueryException(http_code=400, message="An unexpected error occurred while processing your request. The team your are attempting to add this player to may not exist. Please inform your supervisor of this error. Error Code 260")
            
            new_player = ObjectBuilder().convert_player_to_database_type(player=player, team_id=team_id)
            logger.debug(f'Created new player database type with data: {dict(new_player)}')

            self.player_query.create_resource(dk_session=self.session, resource=new_player)

            return Status(status_code=200, message='Successful database insertion')

        except PlayerQueryException as t:
            logger.error(f'Error occurred while querying either team or player tables in database: {t.message}')
            return Status(status_code=t.http_code, message=t.message)

        except Exception as e:
            logger.error(f'An unexpected error occurred while inserting to player or team table in database. Check connection to DK. Error: {e}')
            return Status(
                status_code=500,
                message='An unexpected error occurred while processing your request. Player may already exist. Please inform your supervisor of this error. Error Code 250')

    '''
    Attempts to delete player from database
    Return status object with resulting http code and error message if applicable
    '''
    def delete_from_player_table (self, player_id: str) -> Status:

        try:

            player = self.player_query.get_resource_by_id(dk_session=self.session, id=player_id)

            if player == None:
                raise PlayerQueryException(http_code=400, message=f'Could not find player with id: {player_id}')
            
            self.player_query.delete_resource_by_id(dk_session=self.session, id=player_id)

            return Status(status_code=200, message='Successful table deletion')

        except PlayerQueryException as p:
            logger.error(f'There was an error while querying the player table: {p.message}')
            return Status(status_code=p.http_code, message=p.message)

        except Exception as e:
            logger.error(f'Received unexpected error while querying team table in database: {e}')
            return Status(status_code=500, message='An unexpected error occurred while processing your request. Team may not exist Please inform your supervisor of this error. Error Code 240')

class PlayerQueryException (Exception):

    def __init__ (self, http_code: int, message: str):
        self.http_code = http_code
        self.message = message
