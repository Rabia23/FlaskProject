"""
Models for the Api app
"""

# local imports
from app.db import db


class Wallet(db.Model):
    """
    This class represents the wallet table.
    """

    # Ensures table will be named in plural and not in singular as in
    # the name of the model
    __tablename__ = 'wallets'

    id = db.Column(db.Integer, primary_key=True)
    currency_code = db.Column(db.String(length=3))
    open_exchange_price = db.Column(db.Float(precision=8))
    requested_amount = db.Column(db.Float(precision=8))
    final_amount = db.Column(db.Float(precision=8))
    created_on = db.Column(db.DateTime, index=True, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return '<id: {}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()
