#！coding:utf-8
import pymysql
from time import strftime,localtime,time
import threading
import functools



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
        return self._connect()

class create_engine(object):
    """创建数据库链接connect"""
    def __init__(self,app):
        from pymysql import connect
        global engine
        if engine is not None:
            print u"engine 不为空！",engine
            #raise DBError("Engine is already inited")
        print u"连接数据库链接开始...crate_engine开始执行...数据库地址为：%s" %app.config["MYSQL_HOST"]
        db_info=dict(host=app.config["MYSQL_HOST"],user=app.config["MYSQL_USER"],passwd=app.config["MYSQL_PASSWORD"],port=app.config["MYSQL_PORT"],db=app.config["MYSQL_DB"],)
        engine=_Engine(lambda:connect(host=app.config["MYSQL_HOST"],user=app.config["MYSQL_USER"],passwd=app.config["MYSQL_PASSWORD"],port=app.config["MYSQL_PORT"],db=app.config["MYSQL_DB"]))
        print engine

def db():
    return create_engine


class Connection(object):
    """
    数据库连接变量操作commit,rollback,cursor,close
    """

    def __init__(self):
        self.connection=None
        print u"初始化连接"

    def cursor(self):
        """
        生成数据库游标
        :return: 游标cursor
        """
        print u"正在连接数据库..."
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
            print self.connection
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
        return self.connection is not None

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
        print u"数据库查询线程开始"
        self.should_close=False
        if not _db_.is_init():
            print u"db查询尚未初始化...正在初始化..."
            _db_.init()
            self.should_close=True
        return _db_

    def __exit__(self, exc_type, exc_val, exc_tb):
        print u"数据库查询线程结束"
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
            print u"执行判断"
            return func(*args,**kw)
    return _warpps

def _select(sql,is_first=True,*args):

    global _db_
    cursor=None
    sql=sql.replace("#","%s")  #防注入使用‘#’替换符
    print u"%s：%s" %(current_time(),sql.format(args))
    try:
        cursor=_db_.cursor()
         #数据库语句
        cursor.execute(sql %args)
        if cursor.description:
            names = [x[0] for x in cursor.description]
        if is_first:
            values = cursor.fetchone()
            if not values:
                return None
            return Dict(names, values)
        return [Dict(names, x) for x in cursor.fetchall()]

    # 注释：select>1 >>> [(1, '769007157@qq.com', '541', 'b31da2dac24209ab17ddb36a3ae9cf3535f8db77'), (1, 'nvray@foxmail.com', 'nvray', 'a1c5c80c3ddc9ecdb855f76195b09725cb40a1f1')]



    except Exception,e:
        raise DBError(e)



    finally:
        if cursor:
            print u"已关闭连接"
            cursor.close()



@with_connect
def select_one(sql,*args):
    """
    检索第一个结果
    :return:
    """
    print  _select(sql,True,*args)

@with_connect
def select(sql,*args):
    """
    多个结果

    测试：
    from app.mysql import *
    select_one("select * from users where id=#;",1)
    """
    print _select(sql,False,*args)

@with_connect
def update():
    pass

@with_connect
def insert(table,**kw):
    cols, args = zip(*kw.iteritems())
    sql = 'insert into `%s` (%s) values (%s)' % (table, ','.join(['`%s`' % col for col in cols]), ','.join(['#' for i in range(len(cols))]))
    return _update(sql, *args)




if __name__=="__main__":
    from . import app
    create_engine(app)