#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from wtforms.validators import DataRequired
from wtforms import Form, StringField, SubmitField


class EditForm(Form):
        title = StringField('标题', validators=[DataRequired()])
        content = StringField('内容', validators=[DataRequired()])
        author = StringField('作者')
        submit = SubmitField('提交')
        tags = StringField('标签')


