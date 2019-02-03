__author__ = 'rabia'

# third-party imports
from flask import Flask

# local imports
from . import api
from .api import models
from .db import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    api.init_app(app)

    return app
