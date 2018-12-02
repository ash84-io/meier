# -*- coding: utf-8 -*-
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry
from flask_jwt_extended import JWTManager

db = SQLAlchemy(session_options={'autocommit': False})
sentry = Sentry()
cache = Cache(config={'CACHE_TYPE': 'simple'})
jwt = JWTManager()
