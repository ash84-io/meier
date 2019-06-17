from bs4 import BeautifulSoup
from flask import Flask, render_template

from meier.extensions import cache, db, sentry
from meier.resources.admin.contents.contents_api import admin_contents_api
from meier.resources.admin.contents.contents_view import admin_contents_view
from meier.resources.admin.dashboard.dashborad_view import admin_dashboard_view
from meier.resources.admin.index.index_view import admin_index_view
from meier.resources.admin.settings.settings_api import admin_settings_api
from meier.resources.admin.settings.settings_view import admin_settings_view
from meier.resources.admin.user.user_api import admin_user_api
from meier.resources.admin.user.user_view import admin_user_view
from meier.resources.admin.writer.writer_api import admin_writer_api
from meier.resources.admin.writer.writer_view import admin_writer_view
from meier.resources.blog.assets import assets
from meier.resources.blog.post_detail_view import post_detail_view
from meier.resources.blog.post_list_view import post_list_view
from meier.resources.blog.rss import rss
from meier.resources.blog.tag_list_view import tag_list_view

__all__ = ["create_app"]


def create_app(config_obj="config.ProductionConfig") -> Flask:
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


def configure_blueprints(app) -> None:
    blueprints = [
        assets,
        post_detail_view,
        post_list_view,
        tag_list_view,
        rss,
        admin_contents_api,
        admin_contents_view,
        admin_dashboard_view,
        admin_index_view,
        admin_settings_api,
        admin_settings_view,
        admin_user_api,
        admin_user_view,
        admin_writer_api,
        admin_writer_view,
    ]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_app(app, config_obj="config.ProductionConfig") -> None:
    app.config.from_object(config_obj)


def configure_extensions(app):

    # sentry
    if app.config.get("SENTRY_DSN", None):
        sentry.init_app(app=app, dsn=app.config["SENTRY_DSN"])

    # flask-sqlalchemy
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # flask-cache
    cache.init_app(app)


def configure_error_handlers(app):
    @app.errorhandler(401)
    def unauthorized():
        return render_template("/errors/error.html", status_code=401), 401

    @app.errorhandler(403)
    def forbidden():
        return render_template("/errors/error..html", status_code=403), 403

    @app.errorhandler(404)
    def page_not_found():
        return render_template("/errors/error.html", status_code=404), 404

    @app.errorhandler(500)
    def internal_server_error():
        return render_template("/errors/error.html", status_code=500), 500


def configure_jinja(app):
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True


def configure_filter(app) -> None:
    @app.template_filter("clean")
    def clean_html(raw_html):

        clean_text = BeautifulSoup(raw_html, "lxml").text
        return clean_text

    app.jinja_env.filters["clean"] = clean_html


def configure_dynamic_page(app) -> None:
    from meier.resources.blog.post_detail_view import get_page_view

    with app.app_context():
        from meier.models.post import Post

        all_page = Post.query.filter(Post.is_page.is_(True)).all()
        for page in all_page:
            app.add_url_rule(
                rule="/page/<string:page_name>",
                endpoint=page.post_name,
                view_func=get_page_view,
            )
