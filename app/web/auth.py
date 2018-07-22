#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template, request, flash, url_for, redirect
from app.forms.auth import LoginForm, RegisterForm
from app.models.base import db
from app.models.user import User
from flask_login import logout_user, login_user

from . import web

# 登录
@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and User.query.filter_by(password=form.password.data).first():
            # 保持登录
            login_user(user, remember=True)
            return redirect(url_for('web.mainpage'))
        else:
            flash("账号不存在或密码错误")
    return render_template('auth/login.html', form=form)

# 注册
@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        # 检测用户是否已经注册
        if user.select_register_nickname(form.nickname.data):
            flash("昵称已经被注册")
            return redirect(url_for('web.register'))
        # 检测邮箱是否被注册
        elif user.select_register_email(form.email.data):
            flash("邮箱已经被注册")
            return redirect(url_for('web.register'))

        with db.auto_commit():
            user.set_attrs(form.data)
            db.session.add(user)
            db.session.commit()
            flash("注册成功，请到登录页面登录")
        return redirect(url_for('web.login'))
    else:
        flash("输入信息有误，请重新输入")
    return render_template('auth/register.html', form=form)

# 注销
@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.login'))