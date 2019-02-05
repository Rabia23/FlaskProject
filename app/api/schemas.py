"""
Schemas for the Api app
"""

# local imports
from app.db import marshmallow


class WalletSchema(marshmallow.Schema):
    """
    This class represents the wallet schema.
    """
    class Meta:
        fields = (
            'id', 'currency_code', 'open_exchange_price', 'requested_amount',
            'final_amount', 'created_on', 'updated_on'
        )


# pylint: disable=invalid-name
wallet_schema = WalletSchema()
wallets_schema = WalletSchema(many=True)
