# coding:utf-8
from app import create_app,create_sql
from os import environ
from flask.ext.script import Manager
from app.model import db
config_name = environ.get("APP_NAME") or "MainConfig"
app = create_app(config_name)

manager = Manager(app)


@manager.command
def run():
    create_sql(db)
    app.run("127.0.0.1",8080,True)

if __name__ == "__main__":
    manager.run()
