# coding:utf-8

from flask import Flask
import mysql
from config import config
from .model import Connect
app = Flask(__name__)
db=Connect()
db_=mysql.db()
def create_app(config_name):
    app.config.from_object(config[config_name])
    db_(app)
     #数据库创建,可操作类db执行db.exc("command")

    from views import main
    app.register_blueprint(main)

    return app
