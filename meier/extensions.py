from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

db = SQLAlchemy(session_options={'autocommit': False})
sentry = Sentry()
cache = Cache(config={'CACHE_TYPE': 'simple'})
