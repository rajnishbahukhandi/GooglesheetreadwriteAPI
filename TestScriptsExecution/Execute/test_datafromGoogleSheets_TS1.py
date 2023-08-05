import json
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials
from src.helper.header import common_header
from src.URL.URLs import url_base


# Google Cloud Platform(GCP) - Create A Virtual Machine

class Test_googleSheets(object):

    def setup(self):
        print("Before Test")

    def test_googleSheetTokenVerificcation_TC1(self):

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "../../src/helper/secretkeysJson/apiautomationgcp-secretkey.json", scope)
        client = gspread.authorize(creds)
        current_sheet = client.open('APIVerificationChecklist').sheet1

        # In Google Sheets, use a for loop to choose the range of cells. which begin in the 2nd row and continue to
        # row 16th. In Google Sheet, the user can manually edit ("lastcell = 16") it up to a certain cell range.
        lastcell = 16

        for i in range(2, lastcell + 1):
            user = current_sheet.cell(i, 1, value_render_option='FORMULA').value
            pword = current_sheet.cell(i, 2, value_render_option='FORMULA').value

            payload = json.dumps({
                "emailOrUsername": format(user),
                "password": format(pword)
            })

            response = requests.post(url=url_base(), headers=common_header(), data=payload)

            if response.status_code == 200:
                current_sheet.update_cell(i, 3, 'True')
                current_sheet.update_cell(i, 4, response.status_code)
                current_sheet.update_cell(i, 5, response.json()['token_type'])
                current_sheet.update_cell(i, 6, response.json()['token'])
                current_sheet.update_cell(i, 7, response.json()['expires_at'])
                current_sheet.update_cell(i, 8, response.json()['wow_token'])
            else:
                current_sheet.update_cell(i, 3, 'False')
                current_sheet.update_cell(i, 4, response.status_code)
                current_sheet.update_cell(i, 5, response.json()['message'])

            i += 1

    def tear_down(self):
        print("Complete")
