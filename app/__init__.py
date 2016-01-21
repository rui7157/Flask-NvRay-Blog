# coding:utf-8

from flask import Flask

from config import config
from .model import Connect
app = Flask(__name__)


def create_app(config_name):
    app.config.from_object(config[config_name])

    Connect(app.config["MYSQL_INFO"]).create_db("user")
    from views import main
    app.register_blueprint(main)

    return app
