#coding:utf-8
from hashlib import sha1
"""
    用户名密码加密：将传入的email经过sha1加密后与对应的密码一起再次sha1加密
"""
class Hash(object):
    pwd=sha1()

    def __init__(self,email,password):
        self.pwd.update(email)
        self.username=self.pwd.hexdigest()
        self.password=password

    def en(self):
        self.pwd.update(self.username+self.password)
        return self.pwd.hexdigest()

