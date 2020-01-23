from flask import Blueprint, g, make_response, render_template

from meier.models.settings import Settings
from meier.views.admin.base import login_required_api

admin_user_view = Blueprint(
    "admin_user_view", __name__, url_prefix="/admin/user"
)


@admin_user_view.route("/", methods=["GET"])
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
def login_view():
    return render_template("/admin/login.j2")


@admin_user_view.route("/logout", methods=["GET"])
def logout_view():
    response = make_response(render_template("/admin/login.j2"))
    response.set_cookie("token", "", expires=0)
    return response
