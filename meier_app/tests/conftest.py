import pytest
from flask import g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from meier_app.app import create_app
from meier_app.config import TestingConfig


@pytest.fixture(scope='session')
def flask_app():
    app = create_app('meier_app.config.TestingConfig')
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()


@pytest.fixture(scope='session')
def flask_client(flask_app):
    return flask_app.test_client()


@pytest.fixture(scope='session')
def db():
    engine = create_engine(TestingConfig.SQLALCHEMY_DATABASE_URI, echo=True)
    _session = sessionmaker(bind=engine)
    _db = {'engine': engine, 'session': _session}
    yield _db
    engine.dispose()


@pytest.fixture(scope='function')
def session(db):
    _session = db['session']()
    g.db = _session
    yield _session
    _session.rollback()
    _session.close()


