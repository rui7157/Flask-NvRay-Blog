# coding:utf-8

import pymysql


class Connect:
    """
    说明：
        exc函数执行SQL语句 example:db.exc("select [Colum] from [table] where xx=xx")
        create函数创建数据表   example:db.create([tablename])
        dblog函数保存数据库操作日志 example:db.dblog([path])

    """

    def __init__(self):
        self.dblog=""

    def init_app(self,app):
        try:
            self.conn=pymysql.connect(host=app.config["MYSQL_HOST"],user=app.config["MYSQL_USER"],passwd=app.config["MYSQL_PASSWORD"],port=app.config["MYSQL_PORT"],db=app.config["MYSQL_DB"],)     #connect("127.0.0.1","root","password")
        except Exception,e:
            raise ValueError(u"sql connect fail:%s" %e)
        self.cur=self.conn.cursor()

    def exc(self,comm):
        if not self.conn:
            raise RuntimeError("Failed to create SQL connect! [init_app(app)]")
        from time import strftime,localtime,time
        try:
            result=self.cur.execute("{};".format(comm))
            self.dblog+="执行成功　%s:%s\n" %(strftime('%Y-%m-%d %H:%M:%S',localtime(time())),comm)
        except Exception,e:
            result=False
            self.dblog+="执行失败　%s:%s:%s\n" %(strftime('%Y-%m-%d %H:%M:%S',localtime(time())),comm,e)
        finally:
            print self.dblog
            return result



    def create_db(self,tablename):
        if self.exc("select * from %s;" %tablename):
            print u"表存在"
        else:
            self.exc("create table %s(id int ,email char(20),username char(30),password char(10))" %tablename)
            self.dblog=""

    def __call__(self, *args, **kwargs):
        pass

    def dblog(self,path):
        with open(path,"rw+") as logfile:
            logfile.write(self.dblog)



