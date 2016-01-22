#!conding:u8
from config import config
obj=config["MainConfig"]

class dict_(dict):
    def add(self,obj):
        for key in dir(obj):
            self[key]=getattr(obj,str(key))


configfile=dict_()
print isinstance(configfile,(dict_,dict))
configfile.add(obj)
print configfile