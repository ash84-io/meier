# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_compress import Compress
from raven.contrib.flask import Sentry
db = SQLAlchemy(session_options={'autocommit': False})
login_manager = LoginManager()
compress = Compress()
sentry = Sentry()
