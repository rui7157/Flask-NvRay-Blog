#！coding:utf-8
import pymysql
from time import strftime,localtime,time
import threading
import functools


# class db(object):
#
#     def init_app(self,app):
#         try:
#             self.conn=pymysql.connect(host=app.config["MYSQL_HOST"],user=app.config["MYSQL_USER"],passwd=app.config["MYSQL_PASSWORD"],port=app.config["MYSQL_PORT"],db=app.config["MYSQL_DB"],)     #connect("127.0.0.1","root","password")
#         except Exception,e:
#             raise ValueError(u"sql connect fail:%s" %e)
#         self.cur=self.conn.cursor()
#
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

class create_engine(object):
    """创建数据库链接connect"""

    from pymysql import connect
    def __init__(self,app):
        global engine
        if engine is not None:
            raise DBError("Engine is already inited")
        db_info=dict(host=app.config["MYSQL_HOST"],user=app.config["MYSQL_USER"],passwd=app.config["MYSQL_PASSWORD"],port=app.config["MYSQL_PORT"],db=app.config["MYSQL_DB"],)

        engine=_Engine(lambda:connect(db_info))

def db():
    return create_engine


class Connection(object):
    """
    数据库连接变量操作commit,rollback,cursor,close
    """

    def __init__(self):
        self.connection=None

    def cursor(self):
        """
        生成数据库游标
        :return: 游标cursor
        """
        if self.connection is None:
            self.connection=engine.connect()
        return self.connection.cursor()

    def commit(self):
        try:
            self.connection.commit()
        except Exception:
            self.connection.rollback()

    def rollback(self):
        self.connection.rollback()

    def cleanup(self):
        if self.connection:
            self.connection.close()
            self.connection=None




class Db(threading.local):
    """
    为数据库操作添加线程

    """
    def __init__(self):
        self.connection=None

    def init(self):
        if self.connection is None:
            self.connection=Connection()

    def is_init(self):
        return engine is not None

    def cursor(self):
        return self.connection.cursor()

    def close_db(self):
        self.connection.cleanup()

_db_=Db()


class _Dbconnect(object):
    """
    with 控制打开和关闭连接
    """
    global _db_
    def __enter__(self):
        self.should_close=False
        if not _db_.is_init():
            _db_.init()
            self.should_close=True
        return _db_

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.should_close:
            _db_.close_db()


def current_time():
    """
    :return: 当前时间
    """
    return strftime('%Y-%m-%d %H:%M:%S',localtime(time()))

def with_connect(func):
    """
    自行检查_db_全局变量的打开和关闭,操作完毕自动关闭
    :param func: 数据库操作select insert update...
    """
    @functools.wraps(func)
    def _warpps(*args,**kw):
        with _Dbconnect():
            return func(*args,**kw)
    return _warpps

def _select(sql,is_first=True,*args):
    global _db_
    cursor=None
    sql.replace("#","%s")
    try:
        cursor=_db_.connection.cursor()
        cursor.execute(sql,args)
        print cursor

    except Exception,e:
        print u"%s:数据库语句有误" %current_time() #可记录日志


    finally:
        if cursor:
            cursor.close()




def select_one():
    """
    检索第一个结果
    :return:
    """
    pass

def select():
    """
    多个结果
    :return:
    """
    pass

def update():
    pass

def insert():
    pass




if __name__=="__main__":
    create_engine(app)