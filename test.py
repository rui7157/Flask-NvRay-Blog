class User(object):
    _password = "76900"

    @property
    def password(self):
        print "zhixing"
        raise AttributeError("password not read!")

    @password.setter
    def password(self, password):
        print "setter"
        self._password = password

User(password="123")

print User.password
print User._password
