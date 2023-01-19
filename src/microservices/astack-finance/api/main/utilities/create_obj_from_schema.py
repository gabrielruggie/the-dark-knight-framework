from main.schemas.schemas_admin import *
from main.schemas.schemas_applicant import *
from main.schemas.schemas_response import *
from main.schemas.schemas_transaction_event import *

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
    def build_transaction_event (data: Dict):

        try:
            
            transaction = TransactionEvent(
                first_name=data["first_name"],
                last_name=data["last_name"],
                amount=data["amount"],
                transaction_date=data["date"],
                transaction_time=data['transaction_time'],
                stripe_payer_id=data['stripe_payer_id'],
                physical=data['physical'],
                verified=data['verified'],
                archived=data["archived"]
            )

            return transaction
        
        except Exception as e:
            logger.debug(f'{e}')
    

