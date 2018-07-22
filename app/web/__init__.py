#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Blueprint

web = Blueprint('web', __name__)


from app.web import auth
from app.web import main
from app.web import edit
