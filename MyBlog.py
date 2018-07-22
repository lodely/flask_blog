#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from app import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
