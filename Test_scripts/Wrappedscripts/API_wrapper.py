import json
import requests


# Abstraction and encapsulation
def authToken_response(url, headers, payload):
    auth_response = requests.post(url=url, headers=headers, json=json.dumps(payload))
    return auth_response


def get_response(url, auth, headers, in_json):
    get_response_data = requests.get(url=url, auth=auth, headers=headers)
    if in_json is True:
        return get_response_data.json()
    return get_response_data


def post_response(url, auth, headers, payload, in_json):
    post_response_data = requests.post(url=url, auth=auth, headers=headers, json=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def put_response(url, auth, headers, payload, in_json):
    put_response_data = requests.patch(url=url, auth=auth, headers=headers, json=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data


def patch_response(url, auth, headers, payload, in_json):
    patch_response_data = requests.patch(url=url, auth=auth, headers=headers, json=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def delete_response(url, auth, headers, in_json):
    delete_response_data = requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
