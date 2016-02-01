# coding:utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Required, EqualTo, Email, Length


class LoginForm(Form):
    email = StringField(u"邮箱：", validators=[DataRequired(u"不能为空"), Email(u"邮箱格式错误")])  # ,"用户名格式错误"
    password = PasswordField(u"密码：", validators=[DataRequired(u"不能为空"), Length(6, 16, u"密码长度必须6~16位")])  # ,"密码格式错误"
    submit = SubmitField(u"登陆")


class RegisterForm(Form):
    email = StringField(u"邮箱", validators=[Required(u"不能为空"), Email(u"邮箱格式错误")])
    username = StringField(u"用户名：", validators=[DataRequired(u"不能为空"), Length(3, 20, u"用户名长度必须3~12位")])  # ,"用户名格式错误"
    password = PasswordField(u"密码：", validators=[DataRequired(u"不能为空"), EqualTo(u"password2", u"密码必须一致"),
                                                 Length(6, 16, u"密码长度必须6~16位")])  # ,"密码格式错误"
    password2 = PasswordField(u"再次输入密码：", validators=[DataRequired(u"不能为空")])  # ,"密码格式错误"
    submit = SubmitField(u"注册")
