# coding:utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Required


class LoginForm(Form):
    username = StringField(u"邮箱：", validators=[DataRequired()])  # ,"用户名格式错误"
    password = PasswordField(u"密码：", validators=[DataRequired()])  # ,"密码格式错误"
    submit = SubmitField(u"登陆")


class RegisterForm(Form):
    email = StringField(u"邮箱", validators=[Required()])
