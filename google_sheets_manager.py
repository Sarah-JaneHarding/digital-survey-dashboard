import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsManager:
    def __init__(self, json_keyfile_name, scope):
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_name, scope)
        self.client = gspread.authorize(self.creds)

    def read_sheet(self, sheet_name):
        sheet = self.client.open(sheet_name).sheet1
        return sheet.get_all_records()

    def write_sheet(self, sheet_name, data):
        sheet = self.client.open(sheet_name).sheet1
        sheet.update(data)

    def append_to_sheet(self, sheet_name, row_data):
        sheet = self.client.open(sheet_name).sheet1
        sheet.append_row(row_data)

    def authenticate(self):
        # This function can be called to check if authentication is successful.
        try:
            self.client.list_spreadsheet_files()
            return True
        except Exception as e:
            return False
