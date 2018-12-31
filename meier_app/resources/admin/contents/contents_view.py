# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template, g

from meier_app.commons.logger import logger
from meier_app.models.settings import Settings
from meier_app.extensions import cache
from meier_app.resources.admin.base import login_required_view

admin_contents_view = Blueprint(
    "admin_contents_view", __name__, url_prefix="/admin/contents"
)


@admin_contents_view.route("/", methods=["GET"])
@cache.cached(timeout=86400)
@login_required_view
def get_contents_view():
    settings = Settings.query.first()
    return render_template(
        "/admin/contents.j2",
        title="Contents",
        blog_title=settings.blog_title,
        current_user=g.current_user,
    )
