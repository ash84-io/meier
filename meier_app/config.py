import os

db_host = os.getenv('db_host', "ash84.net")
db_user = os.getenv('db_user', "ash84")
db_password = os.getenv('db_password', "ash8467501!")
sentry_dsn = os.getenv('sentry_dsn', '')


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_MAX_OVERFLOW = -1
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 20
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = 'meier_jwt'
    JWT_TOKEN_LOCATION = 'cookies'
    JWT_COOKIE_SECURE = True
    AES256_KEY = 'MEIER_ENC_KEY_20181202!@#$%^&*()'
    AES256_IV = 'MEIER_IV20181202'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/meier'.format(db_user, db_password, db_host)
    SENTRY_DSN = ''


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/meier'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/meier'
