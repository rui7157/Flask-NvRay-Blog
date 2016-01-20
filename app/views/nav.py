# coding:utf-8
from flask import render_template

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
    from ..model import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print u"服务器收到数据： %s,%s" % (username, password)
    return render_template("login.html", form=form)
