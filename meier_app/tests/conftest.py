import pytest
from meier_app.app import create_app
from mixer.backend.flask import mixer


@pytest.fixture(scope="session")
def flask_app():
    from meier_app.extensions import db as flask_sqlalchemy_db

    app = create_app("meier_app.config.TestingConfig")
    mixer.init_app(app)
    flask_sqlalchemy_db.drop_all(app=app)
    flask_sqlalchemy_db.create_all(app=app)
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()


@pytest.fixture(scope="session")
def flask_client(flask_app):
    return flask_app.test_client()


@pytest.fixture(scope="function")
def session(flask_app):
    from meier_app.extensions import db

    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    _session = db.create_scoped_session(options=options)
    db.session = _session
    mixer.params["session"] = _session
    yield _session
    transaction.rollback()
    connection.close()
    _session.remove()
