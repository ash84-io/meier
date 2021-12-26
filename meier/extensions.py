from flask_sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

db = SQLAlchemy(session_options={"autocommit": False})
sentry = Sentry()
