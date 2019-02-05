"""
Api application file
"""

# local imports
from .routes import api_bp


def init_app(app):
    """
    initialize Api app
    """
    app.register_blueprint(api_bp, url_prefix='/api')
