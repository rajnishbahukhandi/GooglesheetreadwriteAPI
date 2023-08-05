# Assertions: Python assert allow to sanity check the code.
# Common Verification file: Here verify the status code, empty value, null value, lenght of value.
import requests


def verify_http_codeStatus(response_data, expected_data):
    assert response_data.status_code in [200, 201], f'Expected status, but got {response_data.status_code}'


def verify_responseTime(response_data):
    assert response_data.elapsed.total_seconds() < 3
