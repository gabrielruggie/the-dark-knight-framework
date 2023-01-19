from typing import Dict
from main.sheet_scripts.applicant_sheet_edit import ApplicantSheetEditor

from main.utilities.load_env_file import Environment
from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_applicant import Applicant
from main.schemas.schemas_transaction_event import TransactionEvent
from main.schemas.schemas_error import Error

from main.config.event_publisher import EventPublisher
from main.config.event_builder import EventBuilder

from loguru import logger

'''
Note: this consumer will also need to publish a transaction and player
'''
class GoogleTransactionEventConsumer:

    service_id = ''
    admin_id = ''
    full_name_index = {}
    google_topic = Environment.GOOGLE_EVENTS_TOPIC
    postgres_topic = Environment.POSTGRES_EVENTS_TOPIC

    '''
    Connects to Applicant sheet and retrieves data
    Puts data in hash maps for quick lookup time
    '''
    @classmethod
    def __read_applicant_sheet_data (cls):

        try:

            fname_hash = {}

            rows = ApplicantSheetEditor().read_cells()

            count = 2
            for row in rows:
                # First data entry is on row two of google sheet
                app = ObjectBuilder().build_applicant_from_list(data=row, id=count)

                # Filter out all applicants that have already paid
                # Create Key with player's first and last name, this allows a payer to pay for multiple players
                # In /begin-transaction -> have the user fill in the player they are paying for first and last name
                if int(app.amount_owed)> 0:
                    fname_hash.update({f'{app.first_name}-{app.last_name}': dict(app)})
                
                count += 1

            return fname_hash
        
        except Exception as e:
            logger.error(f'There was an error reading applicant google sheet. {e}')
            raise TransactionHandlerException(
                http_code=400, 
                message='An error occurred while reading applicant data sheet. Please inform your supervisor of this error. Error Code: 100'
                )

    '''
    Given a transaction, tries to find the applicant that made the transaction
    in the indexes defined for this class
    '''
    @classmethod
    def __try_find_matches_from_indexes (cls, transaction: TransactionEvent) -> Applicant:

        try:
            
            # Tranaction first and last name is the player's
            name = f'{transaction.first_name}-{transaction.last_name}'
            applicant_found = cls.full_name_index[name]

            if applicant_found == None:
                raise Exception

            app = ObjectBuilder().build_applicant_from_dict(applicant_found)
            return app

        except KeyError:
            logger.warning(f'Applicant: {name} was could not be found in index table.')
            raise TransactionHandlerException(
                http_code=400,
                message=f'Applicant: {name} does not exist!'
                )

    '''
    Create a query to send to the ApplicantSheetEditor to change the applicant's money owed
    if they made a transaction
    '''
    @classmethod
    def __update_applicant_money_owed (cls, row_number: int, new_amount: int):
        
        try:

            write_query = ApplicantSheetEditor().format_query("amount_owed", "amount_owed", [[new_amount]])

            start_col_letter = f'{write_query["start"]}{row_number}'
            end_col_letter = f'{write_query["end"]}{row_number}'

            ApplicantSheetEditor().write_cells(
                start_column=start_col_letter, 
                end_column=end_col_letter, 
                values=write_query["values"],
                value_input_option="USER_ENTERED"
                )
        
        except Exception as e:
            logger.warning(f'There was an error updating applicant data sheet: {e}')
            raise TransactionHandlerException(
                http_code=400,
                message='An error occurred while trying to update the applicant data sheet. Please inform your supervisor of this error. Error Code 110'
                )
    
    @classmethod
    def __add_validated_transaction_to_postgres_topic (cls, transaction: TransactionEvent):

        try:

            event_builder = EventBuilder(
                data=dict(transaction),
                data_type='transaction.add',
                data_source=cls.service_id,
                topic_published_to=cls.postgres_topic,
                publisher_name=cls.admin_id
            )

            transaction_event = event_builder.create()
            publisher = EventPublisher(topic_name=cls.postgres_topic, event=dict(transaction_event))
            publisher.publish()
        
        except Exception:
            logger.error("There was an error while trying to add a new player to the postgres event handler topic. Check connection")
            raise TransactionHandlerException(
                http_code=500,
                message='Error processing transaction. Please inform your supervisor of this error. Error Code 120'
                )
    
    '''
    Adds new player event to postgres event handler topic
    '''
    @classmethod
    def __add_new_player_to_postgres_topic (cls, applicant: Applicant):

        try:

            player = ObjectBuilder().convert_applicant_to_player(applicant=applicant)

            event_builder = EventBuilder(
                data=dict(player),
                data_type='player.add',
                data_source=cls.service_id,
                topic_published_to=cls.postgres_topic,
                publisher_name=cls.admin_id
            )

            player_event = event_builder.create()
            publisher = EventPublisher(cls.postgres_topic, event=dict(player_event))
            publisher.publish()

        except Exception:
            logger.error("There was an error while trying to add a new player to the postgres event handler topic. Check connection")
            raise TransactionHandlerException(
                http_code=500,
                message='Error processing transaction. Please inform your supervisor of this error. Error Code 130'
                )
    
    '''
    Error statuses:
        - 400 -> warning
        - 500 -> internal / logic error
    '''
    @classmethod
    def __create_error (cls, code: int, msg: str, is_cached: int) -> Error:

        try:

            error = Error(
                schema_version='1.0',
                http_code=code,
                msg=msg,
                admin_id=None,
                log_type='warning' if code == 400 else 'error',
                is_cached=is_cached,
                service=None,
                cache_key=None
            )

            return error

        except Exception:
            logger.error('An error occurred while trying to create a new status object. Check status schemas')

    '''
    Consumption process for transaction events
    Returns Error object with http status code embedded within it

    Always returns an Error Object
    '''
    @classmethod
    def process (cls, transaction: TransactionEvent, metadata: Dict) -> Error:
        
        try:
            
            cls.service_id = metadata['service']
            cls.admin_id = metadata['admin']

            # Start by reading applicant sheet data and updating indexes
            cls.full_name_index = cls.__read_applicant_sheet_data()
            
            logger.info("Processing Transaction...")
            applicant = cls.__try_find_matches_from_indexes(transaction=transaction)
            
            t_amount = transaction.amount
            new_amount_owed = applicant.amount_owed - t_amount

            if new_amount_owed <= 0:
                
                # Only create a new player if they are a paid member
                cls.__add_new_player_to_postgres_topic(applicant=applicant)

            else:
                logger.debug(f'Applicant has a remaining balance of: {new_amount_owed}. NOT VALIDATED! Resuming...')

            # Update applicant's amount owed in applicant sheet
            cls.__update_applicant_money_owed(row_number=applicant.id, new_amount=new_amount_owed)

            # Send all transactions to database
            cls.__add_validated_transaction_to_postgres_topic(transaction=transaction)
            logger.info(f'Validated transaction sent to: {cls.postgres_topic}')
            # If is_cached = 0 -> then we don't want to cache status, else yes
            return cls.__create_error(code=200, msg='Successful Transaction Process', is_cached=0)

        except TransactionHandlerException as t:
            logger.error(f'Received a new transaction handler excetpion: {t}')
            return cls.__create_error(code=t.http_code, msg=t.message, is_cached=1)

        except Exception as error:
            logger.error(f'An unexpected error occurred: {error}. Check connection to memory or subscription to topic: {cls.google_topic}')
            return cls.__create_error(
                code=500, 
                msg=f'An unexpected error occurred while trying to process your transaction. Please inform your supervisor of this error. Error Code: 140', 
                is_cached=1
                )

'''
Specialized Expection that contains status code display severity of error
Contains message that will be displayed to the admin
'''
class TransactionHandlerException (Exception):

    def __init__ (self, http_code: int, message: str):
        self.http_code = http_code
        self.message = message
