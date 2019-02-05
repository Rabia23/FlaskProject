"""
Views for the Api app
"""

# third-party imports
from flask_restful import Resource, reqparse

# local imports
from app.utils import response_json, make_request
from app import constants

from .models import Wallet
from .schemas import wallet_schema, wallets_schema


parser = reqparse.RequestParser()  # pylint: disable=invalid-name
parser.add_argument('currency_code', type=str)
parser.add_argument('requested_amount', type=float)
parser.add_argument('no_of_operations', type=int)


class ApiResource(Resource):
    """
    This class represents Api views
    """

    def get(self):

        # parse arguments given in the get call
        args = parser.parse_args()
        currency_code = args['currency_code']
        no_of_operations = args['no_of_operations']

        # return the last N operations for the given currency from the DB
        if currency_code and no_of_operations:
            query = Wallet.query.filter_by(currency_code=currency_code).order_by('-created_on').limit(no_of_operations)  #pylint: disable=line-too-long
            data = wallets_schema.dump(query).data

        # return the last record for the given currency from the DB
        elif currency_code:
            query = Wallet.query.filter_by(currency_code=currency_code).order_by('-created_on').first()  #pylint: disable=line-too-long
            data = wallet_schema.dump(query).data

        # return the last N operations from the DB
        elif no_of_operations:
            query = Wallet.query.order_by('-id').limit(no_of_operations)
            data = wallets_schema.dump(query).data

        # return the last operation stored in DB
        else:
            query = Wallet.query.order_by('-id').first()
            data = wallet_schema.dump(query).data

        if data:
            return response_json(True, data, None)
        else:
            return response_json(True, data, constants.TEXT_DOES_NOT_EXISTS)

    def post(self):

        # parse arguments given in the post call
        args = parser.parse_args()
        currency_code = args['currency_code']
        requested_amount = args['requested_amount']

        # If currency_code or requested_amount is not given in post request
        # body then show parameters missing message to user.
        if not currency_code or not requested_amount:
            return response_json(True, {}, constants.TEXT_MISSING_PARAMS)

        # get the latest forex prices from OpenExchangeRates API
        open_exchange_rates = self.get_open_exchange_rates()

        # If currency_code does not exist in open exchange rates currency codes
        # or negative value is given for requested_amount then show invalid
        # data message to user.
        if currency_code not in open_exchange_rates or requested_amount < 0:
            return response_json(True, {}, constants.INVALID_DATA)

        currency_price = open_exchange_rates[currency_code]

        # create wallet object
        wallet = Wallet(
            currency_code=currency_code,
            open_exchange_price=currency_price,
            requested_amount=requested_amount,
            final_amount=currency_price * requested_amount
        )

        # save the data in database
        wallet.save()

        return response_json(True, wallet_schema.dump(wallet).data, constants.TEXT_OPERATION_SUCCESSFUL)  #pylint: disable=line-too-long

    def get_open_exchange_rates(self):
        """
        :return: latest forex price along with currency codes by calling
        OpenExchangeRates API using python requests library
        """
        open_exchange_data = make_request(constants.OPEN_EXCHANGE_RATES_API_URL)
        return open_exchange_data['rates']
