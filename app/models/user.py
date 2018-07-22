#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from app.models.base import Base, db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from app import login_manager

class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    nickname = Column('nickname', String(24), nullable=False)
    email = Column('email', String(24), nullable=False, unique=True)
    password = Column('password', String(128), nullable=False)
    article_count = Column('article_count', Integer, default=0)

    # 检测用户是否已经注册
    def select_register_email(self, key):
        email = User.query.filter_by(email=key).first()
        return email

    def select_register_nickname(self, key):
        nickname = User.query.filter_by(nickname=key).first()
        return nickname

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))