# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
import traceback
from flask_script import Manager, Server
from meier_app.commons.logger import logger

__all__ = ['create_app']


def create_app():
    app = Flask(__name__, static_url_path="", static_folder="static")
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)
    configure_jinja(app)
    return app


def configure_blueprints(app):
    from meier_app.resources import resource_blueprints
    blueprints = resource_blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_app(app):
    from meier_app.config import meier_config
    app.config['MEIER_CONFIG'] = meier_config

    if 'SQLALCHEMY_DATABASE_URI' in app.config['MEIER_CONFIG']:
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['MEIER_CONFIG']['SQLALCHEMY_DATABASE_URI']
        app.config["SQLALCHEMY_MAX_OVERFLOW"] = -1
        app.config["SQLALCHEMY_ECHO"] = False
        app.config['SQLALCHEMY_POOL_RECYCLE'] = 20


def configure_extensions(app):
    from extensions import db, compress, login_manager
    db.init_app(app)
    compress.init_app(app)
    #login_manager.init_app(app)


def configure_jinja(app):
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True


if __name__ == '__main__':
    try:
        app = create_app()
        manager = Manager(app)
        manager.add_command('runserver', Server(host="0.0.0.0", port=8080))
        manager.run()
    except BaseException:
        logger.exception(traceback.foramt_exc())
