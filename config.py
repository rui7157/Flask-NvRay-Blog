# coding:utf-8
import os


# 配置文件

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nvray secrey_key'

    @staticmethod
    def init_myapp(app):
        print "running Config class"


class MainConfig(Config):
    SECRET_KEY = "key769007157"


config = {
    'MainConfig': MainConfig
}
