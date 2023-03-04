from flask import Blueprint, render_template

from meier.models.settings import Settings
from meier.admin.base import login_required_view

admin_dashboard_view = Blueprint(
    "admin_dashboard_view", __name__, url_prefix="/admin/dashboard"
)


@admin_dashboard_view.route("/", methods=["GET"])
@login_required_view
def get_dashboard_view():
    settings = Settings.query.first()
    return render_template(
        "/admin/dashboard.j2",
        title="DashBoard",
        blog_title=settings.blog_title,
        user_name=None,
    )
