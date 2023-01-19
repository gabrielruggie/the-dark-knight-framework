from main.transaction_event_consumer import PostgresTransactionEventConsumer

from main.team_event_consumer import PostgresTeamEventConsumer
from main.player_event_consumer import PostgresPlayerEventConsumer

from main.schemas.schemas_error import Error

from main.config.cache_connection import connection

from main.utilities.create_obj_from_schema import ObjectBuilder
from main.utilities.serializer import ByteConverter
from main.utilities.resource_loader import ResourceLoader

from loguru import logger

'''
Processes a new event posted to the postgres event handler topic
'''
def process (event, context):

    payload = ByteConverter().deserialize_to_dict(encoded_bytes=event['data'])

    logger.info(f'Deserialized new event to: {payload}')
    resource_loader = ResourceLoader()
    resource_loader.load_service_file()

    # Admin username and micoservice where event originated
    event_source = payload['source']
    event_trigger = payload['trigger']

    # Verify event sender
    if event_source in resource_loader.REGISTERED_SERVICES:
        
        separator_index = payload['type'].index('.')
        event_type = payload['type'][0:separator_index]
        event_action = payload['type'][separator_index+1:]

        # Event data field with specific object details    
        payload_output = eval(payload['data'])

        match event_type:

            # Process All Transaction Events
            case 'transaction':
                
                logger.info(f'Received new transaction event payload to be: {payload_output}')
                logger.info("Processing Transaction Event...")

                match event_action:

                    case 'add':
                        transaction_event = ObjectBuilder().build_transaction_event(data=payload_output)
                        event_handler = PostgresTransactionEventConsumer()
                        error = event_handler.process_add_transaction_request(transaction=transaction_event)

                        # Make sure this was a manual request first
                        if len(event_trigger) > 0 and error.http_code != 200:
                            __cache_error(admin_id=event_trigger, service=event_source, error=error)

                    case 'delete':
                        transaction_id = int(payload_output['transaction_id'])
                        event_handler = PostgresTransactionEventConsumer()
                        error = event_handler.process_delete_transaction_request(transaction_id=transaction_id)

                        # Make sure this was a manual request first
                        if len(event_trigger) > 0 and error.http_code != 200:
                            __cache_error(admin_id=event_trigger, service=event_source, error=error)
                    
                    case _:
                        logger.warning(f'Unrecognized event action: {event_action}')
    
            # Process All Team Events
            case 'team':

                logger.info(f'Received new team event payload to be: {payload_output}')
                logger.info('Processing Team Event...')

                match event_action:

                    case 'add':
                        team_event = ObjectBuilder().build_team_event(data=payload_output)
                        event_handler = PostgresTeamEventConsumer()
                        error = event_handler.process_add_team_request(team=team_event)

                        # Make sure this was a manual request first
                        if len(event_trigger) > 0 and error.http_code != 200:
                            __cache_error(admin_id=event_trigger, service=event_source, error=error)

                    case 'delete':
                        team_id = int(payload_output['team_id'])
                        event_handler = PostgresTeamEventConsumer()
                        error = event_handler.process_delete_team_request(team_id=team_id)

                        # Make sure this was a manual request first
                        if len(event_trigger) > 0 and error.http_code != 200:
                            __cache_error(admin_id=event_trigger, service=event_source, error=error)
                    
                    case _:
                        logger.warning(f'Unrecognized event action: {event_action}')

            # Process All Player Events
            case 'player':

                logger.info(f'Received new player event. Data: {payload_output}')
                
                match event_action:
                    case 'add':
                    
                        player_event = ObjectBuilder().build_player_sheet_event(data=payload_output)
                        event_handler = PostgresPlayerEventConsumer()
                        error = event_handler.process_add_player_request(player=player_event)

                        # Make sure this was a manual request first
                        if len(event_trigger) > 0 and error.http_code != 200:
                            __cache_error(admin_id=event_trigger, service=event_source, error=error)

                    case 'delete':
                        player_id = payload_output['player_id']
                        event_handler = PostgresPlayerEventConsumer()
                        error = event_handler.process_delete_player_request(player_id=player_id)

                        # Make sure this was a manual request first
                        if len(event_trigger) > 0 and error.http_code != 200:
                            __cache_error(admin_id=event_trigger, service=event_source, error=error)
                        
                    case _:
                        logger.warning(f'Unrecognized event action: {event_action}')
            
            case _:
                # If we receive an unknown event type i.e: not transaction, player or team
                logger.warning(f'Received unknown event type: {event_type}. Transaction will be ignored. Please Try Again')

    else:
        logger.warning(f'Unrecognized service sender: {event_source}')

'''
Caches error attached to admin sender
'''
def __cache_error (admin_id: str, service: str, error: Error) -> None:

    error.admin_id = admin_id
    error.service = service
    error.cache_key = f'{admin_id}.{service}.status'

    if connection.get(error.cache_key) == None:
        key = error.cache_key

        status_bytes = ByteConverter().serialize_to_bytes(data=dict(error))
        connection.set(key, status_bytes)
        logger.info('Cached new error created in google sheet scraper cloud function.')
    else:
        logger.warning(f'An error already exists for admin: {admin_id} from service: {service}')
    
