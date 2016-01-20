# coding:utf-8
from app import create_app

app = create_app("MainConfig")

if __name__ == "__main__":
    app.run("127.0.0.1", 8080, debug=True)
