__author__ = 'rabia'

from .routes import api_bp


def init_app(app):
    app.register_blueprint(api_bp, url_prefix='/api')

