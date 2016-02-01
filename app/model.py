# coding:utf-8
from flask.ext.sqlalchemy import SQLAlchemy
from time import strftime, localtime, time
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


def current_time():
    """
    :return: 当前时间
    """
    return strftime('%Y-%m-%d %H:%M:%S', localtime(time()))


class User(db.Model):
    __tablename__ = "users"
    uid = db.Column(db.SmallInteger, primary_key=True)
    uemail = db.Column(db.String(60))
    uname = db.Column(db.String(30))
    upassword_hash = db.Column(db.String(66))

    posts = db.relationship('Post', backref='post', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("password not read!")

    @password.setter
    def password(self, password):
        self.upassword_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.upassword_hash, password)

    def is_authenticated(self):
        """如果用户已经登录,必须返回 True ,否则返回 False"""
        pass
    def is_active(self):
        """如果允许用户登录,必须返回 True ,否则返回 False 。如果要禁用账户,可以返回 False"""
        pass
    def is_anonymous(self):
        """对普通用户必须返回 False"""
        pass
    def get_id(self):
        """必须返回用户的唯一标识符,使用 Unicode 编码字符串"""
        pass


    def __repr__(self):
        return "<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (
            self.__tablename__, self.uid, self.uname, self.uemail, self.upassword_hash)


class Post(db.Model):
    __tablename__ = "posts"
    uid = db.Column(db.SmallInteger, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    author_id = db.Column(db.SmallInteger, db.ForeignKey("users.uid"))
    timestamp = db.Column(db.DateTime(), index=True, default=current_time)

    users = db.relationship("User", backref="user", lazy="joined")
