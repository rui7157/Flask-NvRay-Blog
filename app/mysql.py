#！coding:utf-8
import pymysql
from time import strftime,localtime,time
import threading
class db(object):

    def init_app(self,app):
        try:
            self.conn=pymysql.connect(host=app.config["MYSQL_HOST"],user=app.config["MYSQL_USER"],passwd=app.config["MYSQL_PASSWORD"],port=app.config["MYSQL_PORT"],db=app.config["MYSQL_DB"],)     #connect("127.0.0.1","root","password")
        except Exception,e:
            raise ValueError(u"sql connect fail:%s" %e)
        self.cur=self.conn.cursor()
class Dict(dict):        
    def __init__(self,key,value,**kwargs):
        super(Dict, self).__init__(**kwargs)
        for k,v in zip(key,value):
            self[k]=v


    def __getattr__(self, key):
        if key in self.has_key(key):
            return self[key]
        else:
            raise KeyError("Dict object has not attribute: '%s' ")

    def __setattr__(self, key, value):
        self[key]=value


        
engine=None
class DBError(Exception):
    pass

class _Engine(object):
    def __init__(self,connect):
        self._connect=connect

    def connect(self):
        return self._connect

def create_engine(host="127.0.0.1",user,password,port=3306,database="nvray"):
    from pymysql import connect
    if engine is not None:
        raise DBError("Engine is already inited")
    db_info={host:"127.0.0.1",user=user,password=password,database=database}

    engine=_Engine(lambda:connect(db_info))



def current_time():
    """
    :return: 当前时间
    """
    return strftime('%Y-%m-%d %H:%M:%S',localtime(time()))
