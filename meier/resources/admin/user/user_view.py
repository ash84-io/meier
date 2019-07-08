import traceback

from flask import Blueprint, g, make_response, render_template

from meier.commons.logger import logger
from meier.extensions import cache
from meier.models.settings import Settings
from meier.resources.admin.base import login_required_api

admin_user_view = Blueprint(
    "admin_user_view", __name__, url_prefix="/admin/user"
)


@admin_user_view.route("/", methods=["GET"])
@cache.cached(timeout=86400)
@login_required_api
def get_user_view():
    settings = Settings.query.first()
    return render_template(
        "/admin/user.j2",
        title="User",
        blog_title=settings.blog_title,
        current_user=g.current_user,
    )


@admin_user_view.route("/login", methods=["GET"])
@cache.cached(timeout=86400)
def login_view():
    return render_template("/admin/login.j2")


@admin_user_view.route("/logout", methods=["GET"])
def logout_view():
    try:
        resp = make_response(render_template("/admin/login.j2"))
        resp.set_cookie("token", "", expires=0)
        return resp
    except BaseException:
        logger.exception(traceback.format_exc())
