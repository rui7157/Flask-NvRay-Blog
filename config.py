# coding:utf-8
import os


# 配置文件

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nvray secrey_key'

    @staticmethod
    def init_myapp(app):
        print "running Config class"
class SinaappSae(Config):
    import MySQLdb
    SECRET_KEY = "key769007157"
    MYSQL_HOST=os.environ.get('MYSQL_HOST')
    MYSQL_USER=os.environ.get('ACCESSKEY')
    MYSQL_PASSWORD=os.environ.get('SECRETKEY')
    MYSQL_PORT=int(os.environ.get('MYSQL_PORT'))
    MYSQL_DB = 'app_' + os.environ.get('APPNAME')
    SQLALCHEMY_DATABASE_URI="mysql+MySQLdb://%s:%s@%s/%s" %(os.environ.get('ACCESSKEY'),os.environ.get('SECRETKEY'),os.environ.get('MYSQL_HOST'),'app_' + os.environ.get('APPNAME'))

class MainConfig(Config):
    SECRET_KEY = "key769007157"
    MYSQL_HOST="127.0.0.1"
    MYSQL_USER="root"
    MYSQL_PASSWORD="password"
    MYSQL_PORT=3306
    MYSQL_DB = "nvray"
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:password@127.0.0.1/nvray"


config = {
    'MainConfig': MainConfig
}
