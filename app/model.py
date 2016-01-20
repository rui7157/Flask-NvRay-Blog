# coding:utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Required, EqualTo


class LoginForm(Form):
    email = StringField(u"邮箱：", validators=[DataRequired(), Required("不能为空"), EqualTo("邮箱格式错误")])  # ,"用户名格式错误"
    password = PasswordField(u"密码：", validators=[DataRequired()])  # ,"密码格式错误"
    submit = SubmitField(u"登陆")


class RegisterForm(Form):
    email = StringField(u"邮箱", validators=[Required()])
    username = StringField(u"用户名：", validators=[DataRequired(), Required("不能为空")])  # ,"用户名格式错误"
    password = PasswordField(u"密码：", validators=[DataRequired()])  # ,"密码格式错误"
    password2 = PasswordField(u"再次输入密码：", validators=[DataRequired(), EqualTo("密码必须一致")])  # ,"密码格式错误"
    submit = SubmitField(u"注册")
