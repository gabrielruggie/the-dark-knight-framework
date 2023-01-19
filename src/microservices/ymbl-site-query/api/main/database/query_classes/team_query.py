from typing import List
from main.database.tables.table import Table
from main.database.query_classes.base_query import BaseQuery

from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_team import TeamDatabase

from loguru import logger
from sqlalchemy.orm import Session

from main.schemas.schemas_response import Response

class TeamQuery(BaseQuery[Table.Player, TeamDatabase, TeamDatabase]):
    ...

class ConstructTeamQuery:

    def __init__(self, dk_session: Session):
        self.session = dk_session
        self.team_query = TeamQuery(Table.Team, tablename='team')
    
    # Get all teams from database
    def retrieve_all_teams (self) -> List:

        try:

            data = self.team_query.get_all_resources(dk_session=self.session)
        
            teams = []
            for team in data:
                teams.append(dict(ObjectBuilder().filter_team_standing_fields(data=team)))
            
            return teams

        except Exception as e:
            logger.error(f'{e}')
    
    def create_new_team (self, team_data: TeamDatabase) -> Response:

        try:

            response = self.team_query.create_resource(dk_session=self.session, resource=team_data)
            if response.http_code != 200:
                response = Response(
                    http_code=661,
                    error_code=2,
                    msg=f'An unexpected error occurred while trying to update google cloud database. Please contact your ASTACK administrator if this continues. Error Code: 661-2'
                    )

            logger.info("New team successfully created!")
            return response

        # For unexpected errors. Error response will go through.
        except Exception as e:
            logger.error(f'{e}')

