# coding:utf-8
from re import sub
from flask import render_template, redirect, session, url_for, flash, request, abort
from . import main
from ..model import *
from flask.ext.login import login_user, current_user, logout_user, login_required


@main.route("/")
def index():
    return render_template("index.html")


# -------各大基本视图
@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    print u"页码 %s" % page
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
            page, per_page=3, error_out=False)
    posts = pagination.items
    return render_template("blog.html", posts=posts, pagination=pagination)


@main.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@main.route("/test")
def test():
    user_info = User.query.order_by(User.uid)
    # user_info=user_info.items

    return render_template("test.html", user_info=user_info)


@main.route("/login", methods=["POST", "GET"])
def login():
    from collections import Iterable
    from .forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        session["email"] = sub(r"[-|;|,|/|\(|\)|\[|\]|}|{|%|*|!|=|']", "", form.email.data)  # 过滤email防注入
        session["password"] = form.password.data
        print u"服务器收到数据：" + session.get('email') + session.get('password')
        user = User.query.filter_by(uemail=session.get('email')).first()
        if user:
            if user.verify_password(session.get("email") + session.get("password")):
                flash(u"登陆成功！")
                login_user(user, form.remember_me.data)
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
        user = User(uemail=session.get("email"), password=session.get("email") + session.get("password"),
                    uname=session.get("username"))
        db.session.add(user)
        try:
            db.session.commit()
            flash(u"注册成功！")
            login_user(user)
        except:
            flash(u"注册失败！")
            db.session.rollback()

        return redirect(url_for(".register"))
    return render_template("register.html", form=form)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash(u"成功退出登陆！")
    return redirect(url_for(".index"))


# -------------功能视图---------------
@main.route('/blog/<id>')
def post(id):
    post = Post.query.filter_by(id=id).first()

    return render_template("post.html", post=post)

@main.route("/blog/<id>/delete")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    if post:
        db.session.delete(post)
        try:
            db.session.commit()
            flash(u"删除成功！")
        except:
            flash(u"删除失败！")
            db.session.rollback()
    return redirect(url_for(".blog"))

@main.route("/blog/edit", methods=["POST", "GET"])
@login_required
def editblog():
    from .forms import EditPostForm
    form = EditPostForm()

    if form.validate_on_submit():
        print "test"
        session["title"] = form.title.data
        session["content"] = form.content.data
        print u"服务器收到数据：%s,%s,%s" % (session.get("title"), session.get("content"), current_user.uid)
        post = Post(title=session.get("title"), body=session.get("content"), author_id=current_user.uid)
        db.session.add(post)
        try:
            db.session.commit()
            flash(u"发表成功！")
        except:
            flash(u"发表失败！")
            db.session.rollback()
        return redirect(url_for(".blog"))

    return render_template("editblog.html", form=form)


# -------------错误页面---------------
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
