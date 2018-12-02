# -*- coding:utf-8 -*-
import os
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from flask import Flask
from flask import render_template
from meier_app.extensions import db, cache, sentry, jwt

__all__ = ['create_app']


def create_app(config_obj='config.ProductionConfig'):
    app = Flask(__name__, static_url_path="", static_folder="static")
    configure_app(app, config_obj)
    configure_extensions(app)
    configure_blueprints(app)
    configure_jinja(app)
    configure_filter(app)
    configure_error_handlers(app)
    if not app.testing:
        configure_dynamic_page(app)
    return app


def configure_blueprints(app):
    from meier_app.resources import resource_blueprints
    blueprints = resource_blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_app(app, config_obj='config.ProductionConfig'):
    app.config.from_object(config_obj)


def configure_extensions(app):

    # sentry
    if app.config.get('SENTRY_DSN', None):
        sentry.init_app(app=app,
                        dsn=app.config['SENTRY_DSN'])

    # flask-sqlalchemy
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # flask-cache
    cache.init_app(app)

    # flask-jwt-extended
    jwt.init_app(app)

 
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
        clean_text = BeautifulSoup(raw_html, "lxml").text
        return clean_text

    app.jinja_env.filters['clean'] = clean_html


def configure_dynamic_page(app):
    from meier_app.resources.blog.post_detail_view import get_page_view
    with app.app_context():
        from meier_app.models.post import Post
        all_page = Post.query.filter(Post.is_page.is_(True)).all()
        for page in all_page:
            app.add_url_rule(rule='/page/<string:page_name>', endpoint=page.post_name, view_func=get_page_view)


