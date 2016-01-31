# coding:utf-8
from flask.ext.sqlalchemy import SQLAlchemy
from time import strftime, localtime, time

db = SQLAlchemy()


def current_time():
    """
    :return: 当前时间
    """
    return strftime('%Y-%m-%d %H:%M:%S', localtime(time()))


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.SmallInteger, primary_key=True)
    email = db.Column(db.String(60))
    usernmame = db.Column(db.String(20))
    password_hash = db.Column(db.String(40))

    posts = db.relationship('User', backref='Post', lazy="dynamic")

    def __repr__(self):
        return "<tablename:%s" % self.__tablename__

    @property
    def password(self):
        raise AttributeError("password not read!")

    @password.setter
    def password(self, email, password):
        from views.hash import Hash
        self.password_hash = Hash(email, password).en()


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.SmallInteger, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    timestamp = db.Column(db.DateTime(), index=True, default=current_time())
