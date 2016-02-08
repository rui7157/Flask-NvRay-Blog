# coding:utf-8
import os


# 配置文件

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nvray secrey_key'

    @staticmethod
    def init_myapp(app):
        print "running Config class"

    def __new__(cls):
        if cls.__class__ == "SinaappSae":
            import MySQLdb
        return super(Config, cls).__new__()


class SinaappSae(Config):
    """
    用户名：SAE_MYSQL_USER ， 密码：SAE_MYSQL_PASS

    主库域名：SAE_MYSQL_HOST_M ，端口：SAE_MYSQL_PORT
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('ACCESSKEY')
    MYSQL_PASSWORD = os.environ.get('SECRETKEY')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    SQLALCHEMY_DATABASE_URI = "mysql+MySQLdb://%s:%s@%s:%s/%s" % (
    os.environ.get('SAE_MYSQL_USER'), os.environ.get('SAE_MYSQL_PASS'), os.environ.get('SAE_MYSQL_HOST_M'),
    os.environ.get('SAE_MYSQL_PORT'), os.environ.get('ACCESS_KEY'))


class MainConfig(Config):
    SECRET_KEY = "key769007157"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "password"
    MYSQL_PORT = 3306
    MYSQL_DB = "nvray"
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@127.0.0.1/nvray"


config = {
    'MainConfig': MainConfig,
    'SinaappSae': SinaappSae
}
