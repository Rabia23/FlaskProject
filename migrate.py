"""
Command for running migrations
"""

# third-party imports
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# local imports
from config import DevelopmentConfig
from run import create_app

from app.db import db

# create app object
app = create_app(DevelopmentConfig)  # pylint: disable=invalid-name

# create migrate object to run db migrations
migrate = Migrate(app, db)  # pylint: disable=invalid-name
manager = Manager(app)      # pylint: disable=invalid-name
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
