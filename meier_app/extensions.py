# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from raven.contrib.flask import Sentry
from flask.ext.cache import Cache

db = SQLAlchemy(session_options={'autocommit': False})
login_manager = LoginManager()
sentry = Sentry()
cache = Cache(config={'CACHE_TYPE': 'simple'})
