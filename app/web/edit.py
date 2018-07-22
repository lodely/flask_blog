#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from app.models.base import db
from . import web
from flask import render_template, request
from app.forms.edit_ariticle import EditForm
from flask_login import current_user
from app.models.user import User
from app.models.article import Article



@web.route('/article/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm(request.form)
    uid = current_user.id
    user = User.query.filter_by(id=uid).first()
    form.author.data = user.nickname
    if request.method == 'POST' and form.validate():
        article = Article()
        with db.auto_commit():
            article.set_attrs(form.data)
            db.session.add(article)
            db.session.commit()

    return render_template('edit.html', form=form)