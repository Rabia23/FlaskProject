"""
Main application file
"""

# third-party imports
from flask import Flask

# local imports
from . import api
from .api import models
from .db import db


def create_app(config):
    app = Flask(__name__)
    # load configurations
    app.config.from_object(config)

    # initialize app database
    db.init_app(app)
    # initialize api app
    api.init_app(app)

    return app
