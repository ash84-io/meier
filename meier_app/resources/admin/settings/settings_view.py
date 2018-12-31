# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask import g

from meier_app.resources.admin.base import login_required_view
from meier_app.extensions import cache
from meier_app.models.settings import Settings

admin_settings_view = Blueprint(
    "admin_settings_view", __name__, url_prefix="/admin/settings"
)


@admin_settings_view.route("/", methods=["GET"])
@cache.cached(timeout=86400)
@login_required_view
def get_settings_view():
    settings = Settings.query.first()
    return render_template(
        "/admin/settings.j2",
        title="Settings",
        blog_title=settings.blog_title,
        post_per_page=settings.post_per_page,
        blog_desc=settings.blog_desc,
        theme=settings.theme,
        current_user=g.current_user,
    )
