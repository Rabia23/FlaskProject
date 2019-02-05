"""
Routing urls for the Api app
"""

# third-party imports
from flask import Blueprint
from flask_restful import Api

# local imports
from .resources import ApiResource

# pylint: disable=invalid-name
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(ApiResource, '/last', methods=['GET'], endpoint='last')
api.add_resource(
    ApiResource, '/grab_and_save',
    methods=['POST'],
    endpoint='grab_and_save'
)
