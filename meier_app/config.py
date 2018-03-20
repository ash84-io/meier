class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_MAX_OVERFLOW = -1
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 20
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_MAX_OVERFLOW = -1
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 20
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
