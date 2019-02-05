"""
Command for running the application
"""

# local imports
from config import DevelopmentConfig

from app import create_app

# main entry point of the app
app = create_app(DevelopmentConfig)  # pylint: disable=invalid-name


if __name__ == '__main__':
    app.run()
