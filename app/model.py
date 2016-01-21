# coding:utf-8

import pymysql
#"host":"localhost","user":"root","password":"password","port":3306,"db":"nvray"
class Connect:


    def __init__(self,db_info):
        try:
            self.conn=pymysql.connect(host=db_info["host"],user=db_info["user"],passwd=db_info["password"],port=db_info["port"],db=db_info["db"],)     #connect("127.0.0.1","root","password")
        except Exception,e:
            raise TypeError(u"sql connect fail:%s" %e)
        self.cur=self.conn.cursor()

    def exc(self,comm):
        self.dblog=""
        from time import strftime,localtime,time
        if self.cur.execute(comm):
            self.dblog+="执行成功　%s:%s" %(strftime('%Y-%m-%d %H:%M:%S',localtime(time())),comm)
        else:
            self.dblog+="执行失败　%s:%s" %(strftime('%Y-%m-%d %H:%M:%S',localtime(time())),comm)
        print self.dblog
        return self.dblog

    def create_db(self,tablename):
        if self.exc("select * from %s;" %tablename):
            print u"表存在"
        else:
            self.exc("create table %s(id int ,email char(20),username char(30),password char(10));" %tablename)

    def __call__(self, *args, **kwargs):
        pass



