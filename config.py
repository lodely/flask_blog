#!/usr/bin/env python
# -*- coding: UTF-8 -*-

SECRET_KEY = 'dghaoh2395uy23'
DEBUG = True

# 配置连接的数据库
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/myflaskblog'
SQLALCHEMY_TRACK_MODIFICATIONS = False