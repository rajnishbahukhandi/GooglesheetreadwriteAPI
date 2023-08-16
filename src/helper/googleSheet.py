from oauth2client.service_account import ServiceAccountCredentials
import gspread


def googleSheetOpen():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "../../src/helper/secretkeysJson/apiautomationgcp-secretkey.json", scope)
    client = gspread.authorize(creds)
    current_sheet = client.open('APIVerificationChecklist').sheet1
    return current_sheet
