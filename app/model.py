# coding:utf-8
from flask.ext.sqlalchemy import SQLAlchemy
from time import strftime, localtime, time
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import login_manager




db = SQLAlchemy()


def current_time():
    """
    :return: 当前时间
    """
    return strftime('%Y-%m-%d %H:%M:%S', localtime(time()))


class User(db.Model,UserMixin):
    """
    继承父类UserMixin方法：
    is_authenticated方法是一个误导性的名字的方法，通常这个方法应该返回True，除非对象代表一个由于某种原因没有被认证的用户。
    is_active方法应该为用户返回True除非用户不是激活的，例如，他们已经被禁了。
    is_anonymous方法应该为那些不被获准登录的用户返回True。
    get_id方法为用户返回唯一的unicode标识符。我们用数据库层生成唯一的id。

    """
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

    def get_id(self):
        """
        重写父类UserMixin方法get_id
        """
        return unicode(self.uid)


    def __repr__(self):
        return u"<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (
            self.__tablename__, self.uid, self.uname, self.uemail, self.upassword_hash)


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.SmallInteger, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    author_id = db.Column(db.SmallInteger, db.ForeignKey("users.uid"))
    timestamp = db.Column(db.DateTime(), index=True, default=current_time)

    users = db.relationship("User", backref="user", lazy="joined")



@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))