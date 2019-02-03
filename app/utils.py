__author__ = 'rabia'

import requests


def response_json(success, data, message=None):
    data = {
        "response": data,
        "success": success,
        "message": message,
    }
    return data


def make_request(url):
    req = requests.get(url)
    return req.json()
