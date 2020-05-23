from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    """ General configuration for app is setted by object Config"""
    app.config.from_object(Config)

    return app
