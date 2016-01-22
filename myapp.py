# coding:utf-8
from app import create_app
from os import getenv

config_name=getenv("FLASK_CONFIG_NAME") or "MainConfig"
app = create_app(config_name)

if __name__ == "__main__":
    app.run("127.0.0.1", 8080, debug=True)
