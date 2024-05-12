from flask import Blueprint, g, render_template

from meier.infrastructure.models.settings import Settings
from meier.application.admin.base import login_required_view

admin_contents_view = Blueprint(
    "admin_contents_view", __name__, url_prefix="/admin/contents"
)


@admin_contents_view.route("/", methods=["GET"])
@login_required_view
def get_contents_view():
    settings = Settings.query.first()
    return render_template(
        "/admin/contents.j2",
        title="Contents",
        blog_title=settings.blog_title,
        current_user=g.current_user,
    )
