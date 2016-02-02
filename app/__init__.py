# coding:utf-8

from flask import Flask
from config import config
from flask.ext.login import LoginManager,login_user



app = Flask(__name__)
login_manager=LoginManager()
def create_app(config_name):
    app.config.from_object(config[config_name])
    from model import db
    db.init_app(app)
    login_manager.init_app(app)
    from views import main
    app.register_blueprint(main)

    return app


def create_sql(db):
    db.create_all()

