#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from wtforms import Form, StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# 注册
class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮件不符合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空'),
        Length(6, 20),
        EqualTo('re_password', message='两次输入的密码不一致')])
    re_password = PasswordField(validators=[
        DataRequired(message='密码不可以为空'), Length(6, 20)])
    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    register = SubmitField('注册')

# 登录
class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮件不符合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空'), Length(6, 20)])

    submit = SubmitField('登录')


