from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from main.sheet_scripts.generic_sheet_connect import SheetConnectionFactory

from typing import List, Dict
from loguru import logger

'''
Editor script for the applicant sheet in the offymbl@gmail.com google drive
'''
class ApplicantSheetEditor:

    SHEET_ID = '1j86Q8g1T1DkevHz3x-Cdk02962FJqJ2sCp6ucFsMSCM'
    CREDS = SheetConnectionFactory().get_credentials()

    '''
    Reads all rows and columns from applicant development sheet
    '''
    COLUMN_RANGE = 'A:M'

    '''
    May want to put this in a json file
    '''
    APPLICANT_SHEET_INDEX = {
        "time_stamp":"A",
        "first_name":"B",
        "last_name":"C",
        "email":"D",
        "year":"E",
        "position":"F",
        "number":"G",
        "church":"H",
        "team_level":"I",
        "team_captains_last_name":"J",
        "payer_first_name": "K",
        "payer_last_name": "L",
        "amount_owed": "M"
    }

    '''
    Reads all cells from Applicant Sheet
    Returns a list of rows (individual lists)
    '''
    @classmethod
    def read_cells (cls):

        try:

            service = build('sheets', 'v4', credentials=cls.CREDS)

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=cls.SHEET_ID,
                                        range=cls.COLUMN_RANGE).execute()
            values = result.get('values', [])

            if not values:
                logger.error("Could not connect to applicant development sheet")
                return None 

            # Don't return the headings
            return values[1:]

        except HttpError as err:
            logger.error(f'Could not read data from cells: {err}')
    
    # Writes to particular cells given the start and stop columns as well as values to be put in those cells
    # value_input_option can be either `RAW` or `USER_ENTERED`
    @classmethod
    def write_cells (cls, start_column: str, end_column: str, values: List, value_input_option: str):

        try:

            column_range = f'{start_column}:{end_column}'
            service = build('sheets', 'v4', credentials=cls.CREDS)

            body = {
                'values': values
            }

            result = service.\
                spreadsheets().\
                    values().\
                        update(
                            spreadsheetId=cls.SHEET_ID, range=column_range,
                            valueInputOption=value_input_option, body=body
                            ).\
                                execute()

            logger.info("Applicant sheet updated")
            return result # -> change to payload

        except HttpError as error:
            logger.error(f'Failure to update player sheet. Stopped by: {error}')
    
    # Given applicant attributes, returns a query with the corresponding google sheet columns and the values provided initially
    @classmethod
    def format_query (cls, start_col: str, end_col: str, values: List) -> Dict:

        try:

            query = {
                "start": cls.APPLICANT_SHEET_INDEX[start_col],
                "end": cls.APPLICANT_SHEET_INDEX[end_col],
                "values": values
            }

            return query

        except Exception as e:
            logger.debug(f'Could not find applicant attribute in sheet index. Error: {e}')
            return None