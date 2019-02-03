__author__ = 'rabia'

from flask import Blueprint
from flask_restful import Api

from .resources import ApiResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# route
# api.add_resource(
#     ApiResource,
#     '/last', '/last/<string:currency_code>', '/last/<int:no_of_operations>',
#     '/last/<string:currency_code>/<int:no_of_operations>',
#     methods=['GET'],
#     endpoint='last'
# )
api.add_resource(ApiResource, '/last', methods=['GET'], endpoint='last')
api.add_resource(ApiResource, '/grab_and_save', methods=['POST'], endpoint='grab_and_save')
