from typing import List
from main.database.tables.table import Table
from main.database.query_classes.base_query import BaseQuery

from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_player import PlayerDatabase, PlayerStats
from main.schemas.schemas_response import Response
from main.schemas.schemas_team import TeamDatabase

from loguru import logger
from sqlalchemy.orm import Session

class PlayerQuery(BaseQuery[Table.Player, PlayerDatabase, PlayerStats]):
    ...

class ConstructPlayerQuery:

    def __init__(self, dk_session: Session):
        self.session = dk_session
        self.player_query = PlayerQuery(Table.Player, tablename='player')
    
    # ADD RESPONSE TO THIS!!
    def retrieve_all_players (self) -> List:

        try:

            players = self.player_query.get_all_resources(dk_session=self.session)
            web_players = []

            # Filter database players to fields only relevant to the website
            for player in players:
                web_players.append(dict(ObjectBuilder().filter_player_stat_fields_for_astack(data=player)))

            return web_players
        
        except Exception as e:
            logger.error(f'{e}')
    
    # May have to add database checking of ids before updating
    def update_player_by_id (self, player_dict):
        
        try:
            
            r = self.player_query.update_resource_by_id(resource=player_dict, dk_session=self.session)
            if r.http_code != 200:
                raise Exception("Player Id may not be in database")
            
            logger.info("Player successfully updated in DK")
            return Response(http_code=200, error_code=None, msg="")
            
        except Exception as e:
            logger.error(f'An Error Occurred: {e}')
            return Response(http_code=500, error_code=600, msg="An unexpected error occurred. Please contact your software administrator immediately. Error Code: 600")

    # May have to check each time that a player doesn't exist
    # Again this may not work. May have to research how to do multiple commits in 1 session
    # Player Ids are now team_id + position in form, this adds another random factor to the player_id creation
    def create_players (self, player_name_list: List, team_data: TeamDatabase) -> Response:

        try:

            count = 0
            logger.debug("Before loop")

            team_id = team_data.id
            team_church = team_data.church
            team_level = team_data.school_level
            team_cap_name = team_data.cap_last_name

            for i in range(len(player_name_list)):
                player_split = player_name_list[i].split(" ")
                player_db = PlayerDatabase(
                    id= f'{team_id+i+1}',           # Generate Id by ndx by default
                    first_name=player_split[0],
                    last_name=player_split[1],
                    player_number=0,                # Default value is 0
                    team_id=team_id,
                    team_church=team_church,
                    team_cap_name=team_cap_name,
                    team_level=team_level,
                    tot_points=0,
                    tot_assists=0,
                    tot_rebounds=0,
                    tot_steals=0,
                    tot_blocks=0,
                    games_played=0
                )
                logger.debug("Before query")
                r = self.player_query.create_resource(dk_session=self.session, resource=player_db)
                logger.debug("After query")
                count += 1
            
            logger.debug(f'Created {count} new players!')
            return Response(http_code=200, error_code=0, msg="All players successfully created!")
        
        except Exception as e:
            logger.error(f'{e}')
            return Response(
                http_code=662,
                error_code=3,
                msg='An unexpected error occurred while trying to add one of your players to the cloud database. Please contact your ASTACK administrator if this continues. Error Code: 662-3'
                )