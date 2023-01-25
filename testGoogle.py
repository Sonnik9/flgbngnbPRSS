from __future__ import print_function
from google.auth.transport.requests import Request
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
# import os.path
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.errors import HttpError
# SAMPLE_RANGE_NAME = 'Test List!A2:E246'

class GoogleSheet:
    SPREADSHEET_ID = '1E8ApONqNaH9EXH8eeyOssTC2RNDRFyZ7njVucOnRNPs'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValues(self, range, values):
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=body).execute()
        # print('{0} cells updated.'.format(result.get('totalUpdatedCells')))

        
def main():
   gs = GoogleSheet()
   test_range = 'Test List!G2:H4'
   test_values = [
       [16, 26],
       [36, 46],
       [56, 66]
   ]
   gs.updateRangeValues(test_range, test_values)

if __name__ == '__main__':
    main()
    
    
# python testGoogle.py

# sonnik8719@gmail.com 

# https://docs.google.com/spreadsheets/d/1E8ApONqNaH9EXH8eeyOssTC2RNDRFyZ7njVucOnRNPs/edit#gid=0 

# https://docs.google.com/spreadsheets/d/1E8ApONqNaH9EXH8eeyOssTC2RNDRFyZ7njVucOnRNPs/edit?usp=sharing