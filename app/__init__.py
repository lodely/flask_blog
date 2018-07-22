#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from app.models.base import db
from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    # 调用蓝图
    register_BluePrint(app)

    # 保持用户登录有效
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    # 创建数据库表
    db.init_app(app)
    db.create_all(app=app)
    return app

# 在app中注册web
def register_BluePrint(app):
    from app.web.auth import web
    app.register_blueprint(web)

