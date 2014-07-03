#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path[0:0] = [""]
from flask import Flask
from flask.ext.babel import Babel
from flask import request
#from fedora_college import metadata
from fedora_college.core.constructor import (build_app as build_fedora,
                                             authenticated,
                                             logger, is_admin)


#__version__ = metadata.version
#__author__ = metadata.authors[0]
#__license__ = metadata.license
#__copyright__ = metadata.copyright


LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}


def build_app(app):
    build_fedora(app)
    authenticated()
    logger(app)
    is_admin(app)
    return app


apps = Flask(__name__)
#manager = Manager(app)
babel = Babel(apps)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())


app = build_app(apps)
 
@app.context_processor
def inject_variables():
    user_admin = is_admin(app)

    return dict(
        is_admin=user_admin)

'''
@manager.command
def create_database():
    """Create all database tables"""
    create_db(app)


@manager.command
def drop_database():
    """Create all database tables"""
    drop_db(app)


@manager.command
def run():
    """Run application"""
    app.run(debug=True, host='0.0.0.0')
'''
if __name__ == '__main__':
    #build_app(app)
    #is_admin(app)
    app.run()
    #app.run(debug=True, host='0.0.0.0')
