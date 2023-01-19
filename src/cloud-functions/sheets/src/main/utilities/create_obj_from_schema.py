from main.schemas.schemas_applicant import *
from main.schemas.schemas_payloads import *
from main.schemas.schemas_transaction_event import *
from main.schemas.schemas_player import PlayerSheets

from loguru import logger

from typing import Dict, List

class ObjectBuilder:

    @staticmethod
    def build_transaction_event (data: Dict):

        try:
            
            transaction = TransactionEvent(
                first_name=str(data["first_name"]).lower(),
                last_name=str(data["last_name"]).lower(),
                amount=data["amount"],
                transaction_date=data["transaction_date"],
                transaction_time=data["transaction_time"],
                stripe_payer_id=data['stripe_payer_id'],
                physical=data['physical'],
                verified=data['verified'],
                archived=data["archived"]
            )

            return transaction
        
        except Exception as e:
            logger.warning(f'{e}')
    
    @staticmethod
    def build_applicant_from_dict (data: Dict):

        try:
            applicant = Applicant(
                id=data['id'],
                first_name=str(data['first_name']).lower(),
                last_name=str(data['last_name']).lower(),
                email=data['email'],
                year=str(data['year']).lower(),
                position=str(data['position']).lower(),
                number=data['number'],
                church=str(data['church']).lower(),
                team_level=str(data['team_level']).lower(),
                team_captain_last_name=str(data['team_captain_last_name']).lower(),
                payer_first_name=str(data['payer_first_name']).lower(),
                payer_last_name=str(data['payer_last_name']).lower(),
                amount_owed=data['amount_owed']
            )

            return applicant
        
        except Exception as e:
            logger.warning(f'{e}')
    
    '''
    Starts building from second column to avoid time stamp column
    '''
    @staticmethod
    def build_applicant_from_list (data: List, id: int):

        try:
            applicant = Applicant(
                id=id,
                first_name=str(data[1]).strip().lower(),
                last_name=str(data[2]).strip().lower(),
                email=data[3],
                year=str(data[4]).lower(),
                position=str(data[5]).lower(),
                number=data[6],
                church=str(data[7]).lower(),
                team_level=str(data[8]).lower(),
                team_captain_last_name=str(data[9]).strip().lower(),
                payer_first_name=str(data[10]).strip().lower(),
                payer_last_name=str(data[11]).strip().lower(),
                amount_owed=data[12]
            )

            return applicant
        
        except Exception as e:
            logger.warning(f'{e}')
    
    @staticmethod
    def convert_applicant_to_player (applicant: Applicant) -> PlayerSheets:

        year_code_index = {
            "freshman":1,
            "sophomore":2,
            "junior":3,
            "senior":4
        }

        try:

            is_team_cap = 1 if applicant.team_captain_last_name == applicant.last_name else 0

            player = PlayerSheets(
                first_name=applicant.first_name.strip().lower(),
                last_name=applicant.last_name.strip().lower(),
                email=applicant.email,
                position=applicant.position,
                player_number=applicant.number,
                grade=year_code_index[applicant.year.lower()],
                is_team_captain=is_team_cap,
                team_church=applicant.church.strip().lower(),
                team_cap_name=applicant.team_captain_last_name.strip().lower(),
                team_level=year_code_index[applicant.year.lower()]
            )

            return player

        except Exception as e:
            logger.warning(f'{e}')
