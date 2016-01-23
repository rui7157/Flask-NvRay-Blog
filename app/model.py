# coding:utf-8

import pymysql
from time import strftime,localtime,time

class Connect(object):
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

        """
        如果查询成功返回一个结果数列，查询失败返回False
        :param comm:
        :return:
        """

        if not self.conn:
            raise RuntimeError("Failed to create SQL connect! [init_app(app)]")

        try:
            result=self.cur.execute("{};".format(comm))

            self.dblog+=u"数据库操作执行成功　%s:%s\n" %(strftime('%Y-%m-%d %H:%M:%S',localtime(time())),comm)
            if result:
                return [i for i in self.cur]
        except pymysql.err.ProgrammingError,e:
            result=False
            self.dblog+=u"错误数据库查询语句　%s:%s:%s\n" %(strftime('%Y-%m-%d %H:%M:%S',localtime(time())),comm,e)
        finally:
            print self.dblog
            self.conn.commit()
        return result



    def create_db(self,tablename):
        if self.exc("select * from %s;" %tablename):
            print u"表存在"
        else:
            self.exc("create table %s(id int ,email char(20),username char(30),password char(40))" %tablename)


    def dblog(self,path):
        with open(path,"rw+") as logfile:
            logfile.write(self.dblog)

    #---------------------------------------------------------------------


    def exeUpdate(self,sql):#更新语句，可执行update,insert语句
        sta=self.exc(sql)
        return sta

    def exeDelete(self,IDs): #删除语句，可批量删除
        for eachID in IDs.split(' '):
            sta=self.cur.execute('delete from relationTriple where tID =%d'% int(eachID))
        return sta

    def exeQuery(self,sql):#查询语句

        return self.exc(sql)


    def connClose(self):#关闭所有连接
        self.cur.close()
        self.conn.close()

    def __call__(self, *args, **kwargs):
        #self.create_db("users")
        pass





