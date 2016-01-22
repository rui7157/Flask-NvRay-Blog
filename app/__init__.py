# coding:utf-8

from flask import Flask

from config import config
from .model import Connect
app = Flask(__name__)
db=Connect()

def create_app(config_name):
    app.config.from_object(config[config_name])
    db.init_app(app)
    db.create_db("users")  #数据库创建,可操作类db执行db.exc("command")

    from views import main
    app.register_blueprint(main)

    return app
