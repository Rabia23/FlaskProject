"""
Database configuration file for the application.
"""

# third-party imports
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


# db related variables initialization
# pylint: disable=invalid-name
db = SQLAlchemy()
marshmallow = Marshmallow()
