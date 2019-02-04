__author__ = 'rabia'

from app.db import marshmallow


class WalletSchema(marshmallow.Schema):
    class Meta:
        fields = (
            'id', 'currency_code', 'open_exchange_price', 'requested_amount',
            'final_amount', 'created_on', 'updated_on'
        )


wallet_schema = WalletSchema()
wallets_schema = WalletSchema(many=True)
