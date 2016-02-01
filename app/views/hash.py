# coding:utf-8
from hashlib import sha1

"""
    用户名密码加密：将传入的email经过sha1加密后与对应的密码一起再次sha1加密
"""


class Hash(object):
    def __init__(self, password, email=""):
        self.pwd = sha1()
        self.pwd.update(email)
        self.email_hash = self.pwd.hexdigest()
        self.password = password

    @property
    def en(self):
        self.pwd.update(self.email_hash + self.password)
        return self.pwd.hexdigest()

    @en.setter
    def en(self):
        raise AttributeError("Hash password only read!")
