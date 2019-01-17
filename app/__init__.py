from flask import Flask
from config.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config_name])

    return app
