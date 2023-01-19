from typing import Dict
from main.schemas.schemas_response import *
from main.schemas.schemas_player import *
from main.schemas.schemas_team import *

from loguru import logger

class ObjectBuilder:

    @staticmethod
    def convert_response_to_service_response (response: Response) -> ServiceResponse:

        try: 

            service_response = ServiceResponse(
                schema_version='1.0',
                http_code=response.http_code,
                error_code=response.error_code,
                msg=response.msg
            )

            return service_response
        
        except Exception as e:
            logger.error(f'{e}')
    
    @staticmethod
    def filter_player_stat_fields (data: Dict) -> PlayerWeb:

        try:

            player_web = PlayerWeb(
                first_name=data['first_name'],
                last_name=data['last_name'],
                player_number=data['player_number'],
                team_id=data['team_id'],
                team_church=data['team_church'],
                team_cap_name=data['team_cap_name'],
                team_level=data['team_level'],
                ppg=data['ppg'],
                apg=data['apg'],
                rpg=data['rpg'],
                spg=data['spg'],
                bpg=data['bpg'],
                games_played=data['games_played']
            )

            return player_web
        
        except Exception as e:
            logger.error(f'{e}')
    
    @staticmethod
    def filter_player_stat_fields_for_astack (data: Dict) -> PlayerStats:

        try:

            player_web = PlayerStats(
                id=data['id'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                player_number=data['player_number'],
                team_id=data['team_id'],
                team_church=data['team_church'],
                team_cap_name=data['team_cap_name'],
                team_level=data['team_level'],
                tot_points=data['tot_points'],
                tot_assists=data['tot_assists'],
                tot_rebounds=data['tot_rebounds'],
                tot_steals=data['tot_steals'],
                tot_blocks=data['tot_blocks'],
                games_played=data['games_played']
            )

            return player_web
        
        except Exception as e:
            logger.error(f'{e}')
    
    @staticmethod
    def filter_team_standing_fields (data: Dict) -> TeamWebsite:

        try:

            team_web = TeamWebsite(
                id=data['id'],
                church=data['church'],
                school_level=data['school_level'],
                cap_last_name=data['cap_last_name'],
                wins=data['wins'],
                losses=data['losses']
            )

            return team_web

        except Exception as e:
            logger.error(f'{e}')

