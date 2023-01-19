from main.database.tables.table import Table
from main.database.query_classes.base_query import BaseQuery
from main.schemas.schemas_team import TeamBase, TeamDatabase, TeamUpdate
from main.schemas.schemas_status import Status
from main.utilities.team_id_generator import TeamIdGenerator
from main.utilities.create_obj_from_schema import ObjectBuilder

from loguru import logger
from sqlalchemy.orm import Session

'''
Team table specific query class
'''
class TeamQuery (BaseQuery[Table.Team, TeamDatabase, TeamUpdate]):
    ...

'''
Constructor for the team table specific query class
'''
class ConstructTeamQuery ():

    def __init__ (self, dk_session: Session):
        self.session = dk_session
        self.team_query = TeamQuery(model=Table.Team, tablename='team')
    
    '''
    Attempts to add a new team to the database
    Returns a status payload with result code
    '''
    def insert_into_team_table (self, team: TeamBase) -> Status:

        try:

            id_generator = TeamIdGenerator(church=team.church, school_level=team.school_level, name=team.cap_last_name)
            # Will throw error if id could not be created
            team_id = id_generator.generate()

            # Determine if team already exists:
            retrieved = self.team_query.get_resource_by_id(dk_session=self.session, id=team_id)

            if retrieved != None:
                raise TeamQueryException(http_code=400, message='Team already exists!')
            
            new_team = ObjectBuilder().convert_team_to_database_type(team=team, unique_id=team_id)

            self.team_query.create_resource(dk_session=self.session, resource=new_team)

            return Status(status_code=200, message='Successful table insertion')

        except TeamQueryException as t:
            return Status(status_code=t.http_code, message=t.message)

        except Exception as e:
            logger.error(f'Received unexpected error while querying team table in database: {e}')
            return Status(status_code=500, message='An unexpected error occurred while processing your request. Team may already exist. Please inform your supervisor of this error. Error Code 230')
 
    '''
    Attempts to remove a team from the database given the id of the team
    Returns a status payload with result code
    '''
    def delete_team_from_table (self, team_id: int) -> Status:

        try:

            team = self.team_query.get_resource_by_id(dk_session=self.session, id=team_id)

            if team == None:
                raise TeamQueryException(http_code=400, message=f'Could not find team with id: {team_id}')
            
            self.team_query.delete_resource_by_id(dk_session=self.session, id=team_id)

            return Status(status_code=200, message='Successful table insertion')

        except TeamQueryException as t:
            logger.error(f'Received error while querying team table in database: {t.message}')
            return Status(status_code=t.http_code, message=t.message)

        except Exception as e:
            logger.error(f'Received unexpected error while querying team table in database: {e}')
            return Status(status_code=500, message='An unexpected error occurred while processing your request. Team may not exist Please inform your supervisor of this error. Error Code 240')

class TeamQueryException (Exception):

    def __init__ (self, http_code: int, message: str):
        self.http_code = http_code
        self.message = message