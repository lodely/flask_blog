#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class Article(Base):
    __tablename__ = 'article'
    id = Column('id', Integer, primary_key=True)
    # author = relationship('users')
    uid = Column(Integer, ForeignKey('users.id'))

    title = Column('title', String(128), nullable=False)
    tags = Column('tags', String(18), default='未分组')
    content = Column(Text, nullable=False)
