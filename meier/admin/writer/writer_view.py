from flask import Blueprint, g, render_template

from meier.models.settings import Settings
from meier.admin.base import login_required_view

admin_writer_view = Blueprint(
    "admin_writer_view", __name__, url_prefix="/admin/writer"
)


@admin_writer_view.route("/", methods=["GET"])
@login_required_view
def get_new_writer_view():
    settings = Settings.query.first()
    return render_template(
        "/admin/writer.j2",
        title="Writer",
        blog_title=settings.blog_title,
        current_user=g.current_user,
    )
