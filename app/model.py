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
    uid = db.Column(db.SmallInteger, primary_key=True)
    uemail = db.Column(db.String(60))
    uname = db.Column(db.String(20))
    upassword_hash = db.Column(db.String(40))

    posts = db.relationship('Post', backref='post', lazy="dynamic")

    def __repr__(self):
        return "<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" %(self.__tablename__,self.uid,self.uname,self.uemail,self.upassword_hash)
                   # self.__tablename__,self.uid,self.uemail,self.uname,self.upassword_hash
            # .join([i for i in self.__class__.__dict__.iteritems()])

    @property
    def password(self):
        raise AttributeError("password not read!")

    @password.setter
    def password(self,password):
        from views.hash import Hash
        self.upassword_hash = Hash(password).en
        print Hash(password).en

    def __call__(self):
        return [i for i in self.__class__.__dict__.iteritems()]

class Post(db.Model):
    __tablename__ = "posts"
    uid = db.Column(db.SmallInteger, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    author_id = db.Column(db.SmallInteger, db.ForeignKey("users.uid"))
    timestamp = db.Column(db.DateTime(), index=True, default=current_time)

    users=db.relationship("User",backref="user",lazy="joined")