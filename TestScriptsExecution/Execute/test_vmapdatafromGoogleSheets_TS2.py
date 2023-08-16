import json
import requests
from src.helper.googleSheet import googleSheetOpen
from src.helper.header import common_BearerTokenHeader
from src.URL.URLs import url_base
from src.helper.json import payloadTestdata_faker_put


# Google Cloud Platform(GCP) - Create A Virtual Machine

class Test_googleSheets(object):
    current_excelsheet = googleSheetOpen()

    # In Google Sheet, the user can manually edit ("lastcell = 16" OR Any number exist in sheet row) it up to a
    # certain cell range.
    lastcell = 9

    def setup(self):
        print("Before Test")

    def test_createNew_Vmap_TC1(self):

        # In Google Sheets, use a for loop to choose the range of cells. which begin in the 2nd row and continue to
        # row lastcell.
        for i in range(2, Test_googleSheets.lastcell + 1):
            date = Test_googleSheets.current_excelsheet.cell(i, 1, value_render_option='FORMULA').value
            title = Test_googleSheets.current_excelsheet.cell(i, 2, value_render_option='FORMULA').value

            payload = json.dumps({
                "formTitle": format(title),
                "formDate": format(date)
            })

            response = requests.post(url=url_base(), headers=common_BearerTokenHeader(), data=payload)

            if response.status_code == 200:
                Test_googleSheets.current_excelsheet.update_cell(i, 3, response.json()['status'])
                Test_googleSheets.current_excelsheet.update_cell(i, 4, response.status_code)
                Test_googleSheets.current_excelsheet.update_cell(i, 5, response.json()['message'])
                Test_googleSheets.current_excelsheet.update_cell(i, 6, response.json()['data']['vMapId'])
            else:
                Test_googleSheets.current_excelsheet.update_cell(i, 3, 'False')
                Test_googleSheets.current_excelsheet.update_cell(i, 4, response.status_code)
                Test_googleSheets.current_excelsheet.update_cell(i, 5, response.json()['message'])

    def test_delete_Vmap_TC2(self):
        # In Google Sheets, use a for loop to choose the range of cells. which begin in the 2nd row and continue to
        # row lastcell.
        for i in range(2, Test_googleSheets.lastcell + 1):
            data_vMapId = Test_googleSheets.current_excelsheet.cell(i, 6, value_render_option='FORMULA').value

            if data_vMapId is None:
                pass
            else:
                response = requests.delete(f"{url_base()}{'/{}'.format(data_vMapId)}",
                                           headers=common_BearerTokenHeader())

                if response.status_code == 200:
                    Test_googleSheets.current_excelsheet.update_cell(i, 7, response.json()['status'])
                    Test_googleSheets.current_excelsheet.update_cell(i, 8, response.status_code)
                    Test_googleSheets.current_excelsheet.update_cell(i, 9, response.json()['message'])
                else:
                    Test_googleSheets.current_excelsheet.update_cell(i, 7, 'False')
                    Test_googleSheets.current_excelsheet.update_cell(i, 8, response.status_code)
                    Test_googleSheets.current_excelsheet.update_cell(i, 9, response.json()['message'])

    def test_put_vmap_TC3(self):
        # In Google Sheets, use a for loop to choose the range of cells. which begin in the 2nd row and continue to
        # row lastcell.
        for i in range(2, Test_googleSheets.lastcell + 1):
            data_vMapId = Test_googleSheets.current_excelsheet.cell(i, 6, value_render_option='FORMULA').value
            # Post_message = Test_googleSheets.current_excelsheet.cell(i, 5, value_render_option='FORMULA').value

            if data_vMapId is None:
                # if Post_message in "The form date does not match the format Y-m-d.":

                response = requests.put(f"{url_base()}{'/{}'.format(data_vMapId)}", headers=common_BearerTokenHeader(),
                                        json=payloadTestdata_faker_put())
                if response.status_code == 200:
                    Test_googleSheets.current_excelsheet.update_cell(i, 12, response.json()['status'])
                    Test_googleSheets.current_excelsheet.update_cell(i, 13, response.status_code)
                    Test_googleSheets.current_excelsheet.update_cell(i, 14, response.json()['message'])
                    # Test_googleSheets.current_excelsheet.update_cell(i, 10, payloadTestdata_faker_put().get('formDate'))
                    # Test_googleSheets.current_excelsheet.update_cell(i, 11, payloadTestdata_faker_put().get('formTitle'))
                    # Test_googleSheets.current_excelsheet.update_cell(i, 11, response.json()['data']['formTitle'])

                else:
                    Test_googleSheets.current_excelsheet.update_cell(i, 12, 'False')
                    Test_googleSheets.current_excelsheet.update_cell(i, 13, response.status_code)
                    Test_googleSheets.current_excelsheet.update_cell(i, 14, response.json()['message'])


    def tear_down(self):
        print("Complete")
