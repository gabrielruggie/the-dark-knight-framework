from main.schemas.schemas_payloads import *
from main.schemas.schemas_transaction_event import *

from loguru import logger
from typing import Dict

from main.schemas.schemas_payer import StripePayerEvent

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
            logger.debug(f'{e}')
    
    @staticmethod
    def build_payment_event (data: Dict) -> StripePayerEvent:
        
        try:
                
            pending = StripePayerEvent(
                first_name=str(data["first_name"]).lower(),
                last_name=str(data["last_name"]).lower(),
                amount=data["amount"],
                transaction_date=data["transaction_date"],
                transaction_time=data["transaction_time"],
                status=data["status"],
                payer_id=data["payer_id"]
            )

            return pending

        except Exception as e:
            logger.error(f'{e}')
        
    @staticmethod
    def convert_stripe_event_to_transaction (stripe_event: StripePayerEvent) -> TransactionEvent:

        try:

            transaction = TransactionEvent(
                first_name=stripe_event.first_name,
                last_name=stripe_event.last_name,
                amount=stripe_event.amount,
                transaction_date=stripe_event.transaction_date,
                transaction_time=stripe_event.transaction_time,
                stripe_payer_id=stripe_event.payer_id,
                physical=0,
                verified=0,
                archived=0
            )

            return transaction

        except Exception as e:
            logger.error(f'{e}')