# -*- coding:utf-8 -*-
import os
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from flask import Flask
from flask import render_template
from meier_app.extensions import db, login_manager
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

__all__ = ['create_app']


class BeakerSessionInterface(SessionInterface):
    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session

    def save_session(self, app, session, response):
        session.save()


def create_app():
    app = Flask(__name__, static_url_path="", static_folder="static")
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)
    configure_jinja(app)
    configure_filter(app)
    configure_error_handlers(app)
    return app


def configure_blueprints(app):
    from meier_app.resources import resource_blueprints
    blueprints = resource_blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_app(app):
    app.config.from_object('config.DevelopmentConfig')


def configure_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # flask-login
    login_manager.login_view = "/admin/user/login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(token):
        # logger.debug('load_user:{}'.format(token))
        from meier_app.models import User
        return User.get_from_token(token)

    session_opts = {
        'session.type': 'ext:database',
        'session.url': app.config['SQLALCHEMY_DATABASE_URI'],
        'session.cookie_expires': True,
        'session.httponly': True,
        #'session.secure': True,
        'session.timeout': 43200,
        'session.sa.pool_recycle': 250
    }
    app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.session_interface = BeakerSessionInterface()


def configure_error_handlers(app):
    @app.errorhandler(401)
    def unauthorized(error):
        return render_template("/errors/error.html", status_code=401), 401

    @app.errorhandler(403)
    def forbidden(error):
        return render_template("/errors/error..html", status_code=403), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("/errors/error.html", status_code=404), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("/errors/error.html", status_code=500), 500


def configure_jinja(app):
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True


def configure_filter(app):
    @app.template_filter('numbers')
    def numbers(amt):
        """
        금액에 대한 쉼표(,) 처리

        :param amt: 금액
        :return: 쉼표(,) 구분된 금액 문자열
        """
        if amt:
            import locale
            locale.setlocale(locale.LC_ALL, 'ko_KR')
            return locale.format("%d", int(amt), grouping=True)
        return amt

    app.jinja_env.filters['numbers'] = numbers

    @app.template_filter('clean')
    def clean_html(raw_html):
        from bs4 import BeautifulSoup
        cleantext = BeautifulSoup(raw_html, "lxml").text
        return cleantext

    app.jinja_env.filters['clean'] = clean_html


app = create_app()
app.run(host='0.0.0.0', port=7878)

