from flask_restful import Resource, reqparse
from .models import Wallet
from .schemas import wallet_schema, wallets_schema
from app.db import db
from app.utils import response_json, make_request
from app import constants

parser = reqparse.RequestParser()
parser.add_argument('currency_code', type=str)
parser.add_argument('requested_amount', type=float)
parser.add_argument('no_of_operations', type=int)


class ApiResource(Resource):

    def get(self):
        args = parser.parse_args()
        currency_code = args['currency_code']
        no_of_operations = args['no_of_operations']

        if currency_code and no_of_operations:
            query = Wallet.query.filter_by(currency_code=currency_code).order_by('-created_on').limit(no_of_operations)
            data = wallets_schema.dump(query).data

        elif currency_code:
            query = Wallet.query.filter_by(currency_code=currency_code).order_by('-created_on').first()
            data = wallet_schema.dump(query).data

        elif no_of_operations:
            query = Wallet.query.order_by('-id').limit(no_of_operations)
            data = wallets_schema.dump(query).data

        else:
            query = Wallet.query.order_by('-id').first()
            data = wallet_schema.dump(query).data

        if data:
            return response_json(True, data, None)
        else:
            return response_json(True, data, constants.TEXT_DOES_NOT_EXISTS)

    def post(self):
        args = parser.parse_args()
        currency_code = args['currency_code']
        requested_amount = args['requested_amount']

        if not currency_code or not requested_amount:
            return response_json(True, {}, constants.TEXT_MISSING_PARAMS)

        open_exchange_rates = self.get_open_exchange_rates()
        if currency_code not in open_exchange_rates or requested_amount < 0:
            return response_json(True, {}, constants.INVALID_DATA)

        currency_price = open_exchange_rates[currency_code]
        wallet = Wallet(
            currency_code=currency_code,
            open_exchange_price=currency_price,
            requested_amount=requested_amount,
            final_amount=currency_price * requested_amount
        )
        db.session.add(wallet)
        db.session.commit()

        result = wallet_schema.dump(wallet).data

        return response_json(True, result, constants.TEXT_OPERATION_SUCCESSFUL)

    def get_open_exchange_rates(self):
        open_exchange_data = make_request(constants.OPEN_EXCHANGE_RATES_API_URL)
        return open_exchange_data['rates']

