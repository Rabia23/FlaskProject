"""
Helper methods
"""

# third-party imports
import requests


def response_json(success, data, message=None):
    """
    Helper method that converts the given data in json format
    :param success: status of the APIs either true or false
    :param data: data returned by the APIs
    :param message: user-friendly message
    :return: json response
    """
    data = {
        "response": data,
        "success": success,
        "message": message,
    }
    return data


def make_request(url):
    """
    Helper method that uses Python Requests library to make calls to
    external APIs
    :param url: url on which request can make
    :return: data returned by requests library in the json format
    """
    req = requests.get(url)
    return req.json()
