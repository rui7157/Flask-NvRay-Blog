# coding:utf-8
from app import create_app
from os import getenv
from flask.ext.script import Manager

config_name = getenv("FLASK_CONFIG_NAME") or "MainConfig"
app = create_app(config_name)
manager = Manager(app)


@manager.command
def mysqlshell():
    pass

if __name__ == "__main__":
    manager.run()
