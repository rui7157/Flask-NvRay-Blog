#!coding:u8
class cls(object):
    co=0
    def __init__(self):
        print "obj co=%d" %(self.co+1)
        print "cls co=%d" %(cls.co+1)
        print self.__class__


def ad(obj):
    return obj.co
t=cls()
t2=cls()
print t.co