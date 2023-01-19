from main.schemas.schemas_response import *
from main.schemas.schemas_player import PlayerSheets
from main.schemas.schemas_admin import *

from loguru import logger

from typing import Dict

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
    def build_admin_base (data: Dict):

        try:

            admin = AdminDarkKnightBase(
                username=data['username'],
                astack_right_level=data['right_level']
            )

            return admin
        
        except Exception as e:
            logger.error(f'{e}')

    @staticmethod
    def format_new_player_input (player: PlayerSheets):

        try:

            player_fmt = PlayerSheets(
                first_name=player.first_name.lower().strip(),
                last_name=player.last_name.lower().strip(),
                email=player.email.strip(),
                position=player.position.lower().strip(),
                player_number=player.player_number,
                grade=player.grade,
                is_team_captain=player.is_team_captain,
                team_church=player.team_church.lower().strip(),
                team_cap_name=player.team_cap_name.lower().strip(),
                team_level=player.team_level
            )

            return player_fmt
        
        except Exception as e:
            logger.error(f'{e}')

