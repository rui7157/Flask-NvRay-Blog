# coding:utf-8
from flask import render_template, redirect, session, url_for

from . import main


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
    from .forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        session["email"] = form.email.data
        session["password"] = form.password.data
        print u"服务器收到数据： %s,%s" % (session.get("email"), session.get("password"))
        return redirect(url_for(".login"))
    return render_template("login.html", form=form)


@main.route("/register", methods=["POST", "GET"])
def register():
    from .forms import RegisterForm
    form = RegisterForm()
    if form.validate_on_submit():
        session["email"] = form.email.data
        password["password"] = form.password.data
        username["username"] = form.username.data
        print u"服务器收到数据： %s,%s,%s" % (session.get("email"), session.get("username"), session.get("password"))
        return redirect(url_for(".register"))
    return render_template("register.html", form=form)
