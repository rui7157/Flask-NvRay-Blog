import functools
class ceshi(object):
    def zs(self,func):
        @functools.wraps(func)
        def jia(*kw,**args):
            print dir(func)

            return func(*kw,**args)
        return jia
c=ceshi()
@c.zs
class g(object):
    def __call__(self, k):
        print k


g()