import sentry_sdk
from bs4 import BeautifulSoup
from flask import Flask, abort, render_template
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.exceptions import BadRequest, NotFound

from meier import __version__
from meier.config import Config
from meier.extensions import cache, db
from meier.views.admin.contents.contents_api import admin_contents_api
from meier.views.admin.contents.contents_view import admin_contents_view
from meier.views.admin.dashboard.dashborad_view import admin_dashboard_view
from meier.views.admin.index.index_view import admin_index_view
from meier.views.admin.settings.settings_api import admin_settings_api
from meier.views.admin.settings.settings_view import admin_settings_view
from meier.views.admin.user.user_api import admin_user_api
from meier.views.admin.user.user_view import admin_user_view
from meier.views.admin.writer.writer_api import admin_writer_api
from meier.views.admin.writer.writer_view import admin_writer_view
from meier.views.blog.assets import assets
from meier.views.blog.post_detail_view import post_detail_view
from meier.views.blog.post_list_view import post_list_view
from meier.views.blog.rss import rss
from meier.views.blog.tag_list_view import tag_list_view

__all__ = ["create_app"]


def create_app(config: Config) -> Flask:
    app = Flask(__name__, static_url_path="", static_folder="static")
    configure_app(app, config)
    configure_extensions(app, config)
    configure_blueprints(app)
    configure_jinja(app)
    configure_filter(app)
    configure_error_handlers(app)
    if not app.testing:
        configure_dynamic_page(app)
    app.url_map.strict_slashes = False
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


def configure_app(app, config: Config) -> None:
    app.config.from_object(config)
    app.config["MYSQL_DATABASE_CHARSET"] = "utf8mb4"


def configure_extensions(app, c: Config) -> None:

    # sentry
    if c.sentry_dsn:
        sentry_sdk.init(
            dsn=c.sentry_dsn,
            integrations=[FlaskIntegration()],
            release=__version__,
        )

    # flask-sqlalchemy
    connection_string = (
        f"{c.db_user}:{c.db_password}@{c.db_host}/{c.db_name}?charset=utf8mb4"
    )
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{connection_string}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # flask-cache
    cache.init_app(app)


def configure_error_handlers(app) -> None:
    @app.errorhandler(BadRequest)
    def handle_bad_request(_):
        abort(400)

    @app.errorhandler(NotFound)
    def handler_not_found(_):
        abort(404)

    @app.errorhandler(401)
    def unauthorized(_):
        return render_template("/errors/error.html", status_code=401), 401

    @app.errorhandler(403)
    def forbidden(_):
        return render_template("/errors/error..html", status_code=403), 403

    @app.errorhandler(404)
    def page_not_found(_):
        return render_template("/errors/error.html", status_code=404), 404

    @app.errorhandler(500)
    def internal_server_error(_):
        return render_template("/errors/error.html", status_code=500), 500


def configure_jinja(app) -> None:
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True


def configure_filter(app) -> None:
    @app.template_filter("clean")
    def clean_html(raw_html):
        clean_text = BeautifulSoup(raw_html, "lxml").text
        return clean_text

    app.jinja_env.filters["clean"] = clean_html


def configure_dynamic_page(app) -> None:
    from meier.views.blog.post_detail_view import get_page_view

    with app.app_context():
        from meier.models.post import Post

        all_page = Post.query.filter(Post.is_page.is_(True)).all()
        for page in all_page:
            app.add_url_rule(
                rule="/page/<string:page_name>",
                endpoint=page.post_name,
                view_func=get_page_view,
            )
