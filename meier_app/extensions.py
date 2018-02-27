# -*- coding: utf-8 -*-
# FLASK-EXT
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_compress import Compress

# FLASK_SQLALCHEMY
db = SQLAlchemy(session_options={'autocommit': False})

# FLASK_LOGIN
login_manager = LoginManager()

# FLASK COMPRESS
compress = Compress()
