from google.oauth2 import service_account

'''
Creates a connection to a spread sheet found in the offymbl@gmail.com google drive
'''
class SheetConnectionFactory:

    def __init__ (self):
        self.scope = ['https://www.googleapis.com/auth/spreadsheets']
        self.creds_path = './credentials.json'
    
    def get_credentials (self):
        return service_account.Credentials.from_service_account_file(self.creds_path, scopes=self.scope)