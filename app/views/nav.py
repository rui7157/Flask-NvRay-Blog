# coding:utf-8
from re import sub
from flask import render_template, redirect, session, url_for
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
    return render_template("test.html")


@main.route("/login", methods=["POST", "GET"])
def login():
    from collections import Iterable
    from .forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        session["email"] = sub(r"[-|;|,|/|\(|\)|\[|\]|}|{|%|*|!|=|']", "", form.email.data)  # 过滤email防注入
        session["password"] = form.password.data
        print u"服务器收到数据：" + session.get('email') + session.get('password')
        querydata = db.exeQuery("select password from users where email='%s'" % (session.get('email')))
        if querydata is not False and querydata[0][0] == Hash(form.password.data, form.password.data).en():
            print "登陆成功"
        else:
            print "登陆失败"
        return redirect(url_for(".login"))
    return render_template("login.html", form=form)


@main.route("/register", methods=["POST", "GET"])
def register():
    from .forms import RegisterForm

    form = RegisterForm()
    if form.validate_on_submit():
        session["email"] = form.email.data
        session["password"] = form.password.dat
        session["username"] = form.username.data
        print u"服务器收到数据： %s,%s,%s" % (session.get("email"), session.get("username"), session.get("password"))
        user = User(email=session.get("email"), password=session.get("password"), username=session.get("username"))
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return redirect(url_for(".register"))
    return render_template("register.html", form=form)
