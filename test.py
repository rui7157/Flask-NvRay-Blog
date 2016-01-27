#!coding:utf-8
def add(self,value):
    self["de"]=value

class MyMetaclass(type):
    def __new__(cls,name, base,args):
        if "__tablename__" not in args:
            args["__tablename__"]=name.lower()
        return type.__new__(cls,name,base,args)

class MyDict(dict):
    __metaclass__ = MyMetaclass
    def __init__(self,**kw):
        super(MyDict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):

        self[key]=value


class User(MyDict):
    __tablename__="users"
print User.__subclasses__()


print User.__tablename__
print User.__bases__

print User().__tablename__
