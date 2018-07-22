#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template
from . import web
from app.view_models.article import ArticleViewModel, ArticleCollection
from flask_login import current_user, login_required

@web.route('/main', methods=['GET', 'POST'])
@login_required
def mainpage():
    uid = current_user.id
    return render_template('main.html')

@web.route('/articles', methods=['GET', 'POST'])
@login_required
def articles():
    uid = current_user.id
    articles = ArticleCollection(uid)
    articles.fill()
    return render_template('main.html', articles=articles)

@web.route('/article/detail/<aid>', methods=['GET', 'POST'])
@login_required
def article_detail(aid):
    article = ArticleViewModel()
    pass