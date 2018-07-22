#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from app.models.article import Article
from flask_login import current_user

class ArticleViewModel:
    def __init__(self, article):
        self.title = article.title
        self.author = article.author
        self.create_time = article.create_time
        self.content = article.content
        self.tags = article.tags

    @property
    def Details(self):
        details = {
            'title' : self.title,
            'author' : self.author,
            'create_time' : self.create_time,
            'content' : self.content,
            'tags' : self.tags
        }
        return details

class ArticleCollection:
    def __init__(self, uid):
        self.total = 0
        self.articles = []
        self.uid = uid
    # 查询当前用户所写的所有文章
    def fill(self):
        for article in Article.query.filter_by(uid=self.uid).all():
            self.total += 1
            self.articles.append(ArticleViewModel(article))





