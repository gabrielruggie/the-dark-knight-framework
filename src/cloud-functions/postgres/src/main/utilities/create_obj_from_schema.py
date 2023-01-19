from main.schemas.schemas_error import Error
from main.schemas.schemas_status import Status
from main.schemas.schemas_transaction_event import *
from main.schemas.schemas_team import *
from main.schemas.schemas_player import *

from loguru import logger
from typing import Dict

'''
Creates objects from dictionary contents based on predefined schemas
'''
class ObjectBuilder:

    @staticmethod
    def build_transaction_event (data: Dict) -> TransactionEvent:

        try:
            
            transaction = TransactionEvent(
                first_name=str(data["first_name"]).lower(),
                last_name=str(data["last_name"]).lower(),
                amount=data["amount"],
                transaction_date=data["transaction_date"],
                transaction_time=data['transaction_time'],
                stripe_payer_id=data['stripe_payer_id'],
                physical=data['physical'],
                verified=data['verified'],
                archived=data["archived"]
            )

            return transaction
        
        except Exception as e:
            logger.debug(f'{e}')
    
    @staticmethod
    def convert_transaction_to_database_type (transaction: TransactionEvent, next_id: int) -> TransactionDatabase:

        try:

            transaction_db = TransactionDatabase(
                id=next_id,
                first_name=str(transaction.first_name).lower(),
                last_name=str(transaction.last_name).lower(),
                amount=transaction.amount,
                transaction_date=transaction.transaction_date,
                transaction_time=transaction.transaction_time,
                stripe_payer_id=transaction.stripe_payer_id,
                physical=transaction.physical,
                verified=1,
                archived=0
            )

            return transaction_db
        
        except Exception as e:
            logger.debug(f'{e}')
    
    @staticmethod
    def build_team_event (data: Dict) -> TeamBase:

        try:

            team = TeamBase(
                church=str(data['church']).lower(),
                school_level=data['school_level'],
                cap_last_name=str(data['cap_last_name']).lower()
            )

            return team
        
        except Exception as e:
            logger.error(f'{e}')
    
    @staticmethod
    def convert_team_to_database_type (team: TeamBase, unique_id: int) -> TeamDatabase:

        try:

            team_db = TeamDatabase(
                id=unique_id,
                church=str(team.church).lower(),
                school_level=int(team.school_level),
                cap_last_name=str(team.cap_last_name).lower(),
                wins=0,
                losses=0,
                total_pts=0,
                pts_allowed=0
            )

            return team_db
        
        except Exception as e:
            logger.error(f'{e}')

    @staticmethod
    def build_player_sheet_event (data: Dict) -> PlayerSheets:

        try:

            player = PlayerSheets(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                position=data['position'],
                player_number=data['player_number'],
                grade=data['grade'],
                is_team_captain=data['is_team_captain'],
                team_church=data['team_church'],
                team_cap_name=data['team_cap_name'],
                team_level=data['team_level']
            )

            return player
        
        except Exception as e:
            logger.warning(f'{e}')
    
    @staticmethod
    def convert_player_to_database_type (player: PlayerSheets, team_id: int) -> PlayerDatabase:
        
        try:
            
            player_db = PlayerDatabase (
                id=f'{team_id}-{player.player_number}',
                first_name=player.first_name,
                last_name=player.last_name,
                email=player.email,
                position=player.position,
                player_number=player.player_number,
                grade=player.grade,
                is_team_captain=player.is_team_captain,
                team_church=player.team_church,
                team_cap_name=player.team_cap_name,
                team_level=player.team_level,
                team_id=team_id,
                ppg="",
                apg="",
                rpg="",
                spg="",
                bpg="",
                tot_points=0,
                tot_assists=0,
                tot_rebounds=0,
                tot_steals=0,
                tot_blocks=0,
                games_played=0
            )

            return player_db
        
        except Exception as e:
            logger.warning(f'{e}')
    
    @staticmethod
    def convert_status_to_error (status: Status) -> Error:

        try:

            error = Error(
                schema_version='1.0',
                http_code=status.status_code,
                msg=status.message,
                admin_id=None,
                log_type='warning' if status.status_code == 400 else 'error',
                is_cached=1,
                service=None,
                cache_key=None
            )

            return error
        
        except Exception as e:
            logger.error(f'Received unexpected error while creating new error object: {e}')
            return None