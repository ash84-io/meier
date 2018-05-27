import os

db_host = os.getenv('db_host', None)
db_user = os.getenv('db_user', None)
db_password = os.getenv('db_password', None)

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_MAX_OVERFLOW = -1
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 20
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/meier'.format(db_user, db_password, db_host)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/meier'.format(db_user, db_password, db_host)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/meier_test'.format(db_user, db_password, db_host)
