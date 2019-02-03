from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.db import db
from config import DevelopmentConfig
from run import create_app

app = create_app(DevelopmentConfig)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
