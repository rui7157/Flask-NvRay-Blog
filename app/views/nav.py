# coding:utf-8
from re import sub
from flask import render_template, redirect, session, url_for,flash
from . import main
from hash import Hash
from ..model import *


@main.route("/")
def index():
    return render_template("index.html")


# -------各大基本视图
@main.route("/blog")
def blog():
    return render_template("blog.html")


@main.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@main.route("/test")
def test():
    user_info=User.query.order_by(User.uid)
    # user_info=user_info.items

    return render_template("test.html",user_info=user_info)


@main.route("/login", methods=["POST", "GET"])
def login():
    from collections import Iterable
    from .forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        session["email"] = sub(r"[-|;|,|/|\(|\)|\[|\]|}|{|%|*|!|=|']", "", form.email.data)  # 过滤email防注入
        session["password"] = form.password.data
        print u"服务器收到数据：" + session.get('email') + session.get('password')
        user=User.query.filter_by(uemail=session.get('email')).first()
        if user:
            if user.verify_password(session.get("email")+session.get("password")):
                flash(u"登陆成功！")
            else:
                flash(u"密码错误！")
        else:
            flash(u"该用户不存在！")
        return redirect(url_for(".login"))
    return render_template("login.html", form=form)


@main.route("/register", methods=["POST", "GET"])
def register():
    from .forms import RegisterForm

    form = RegisterForm()
    if form.validate_on_submit():
        session["email"] = form.email.data
        session["password"] = form.password.data
        session["username"] = form.username.data
        print u"服务器收到数据： %s,%s,%s" % (session.get("email"), session.get("username"), session.get("password"))
        user = User(uemail=session.get("email"), password=User(uemail=session.get("email")+session.get("password"), uname=session.get("username"))
        db.session.add(user)
        try:
            db.session.commit()
            flash(u"注册成功！")
        except:
            print "失败！"
            db.session.rollback()

        return redirect(url_for(".register"))
    return render_template("register.html", form=form)
