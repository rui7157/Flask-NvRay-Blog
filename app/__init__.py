# coding:utf-8

from flask import Flask

from config import config

app = Flask(__name__)


def create_app(config_name):
    app.config.from_object(config[config_name])
    from views import main
    app.register_blueprint(main)

    return app
