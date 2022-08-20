from flask import Blueprint, request

from meier.commons.response_data import HttpStatusCode, ResponseData
from meier.extensions import db
from meier.models.settings import Settings
from meier.views.admin import base
from meier.views.admin.base import login_required_api

admin_settings_api = Blueprint(
    "admin_settings_api", __name__, url_prefix="/admin/settings/api"
)


@admin_settings_api.route("/blog_info", methods=["GET"])
@login_required_api
@base.exc_handler
def get_settings_blog_info():
    settings = Settings.query.first()
    return ResponseData(
        code=HttpStatusCode.SUCCESS, data=settings.for_dict
    ).json


@admin_settings_api.route("/blog_info", methods=["POST"])
@login_required_api
@base.exc_handler
def set_settings_blog_info():
    req_data = request.get_json()
    settings = Settings.query.first()

    blog_title = req_data.get("blog_title", "")
    blog_desc = req_data.get("blog_desc", "")
    post_per_page = req_data.get("post_per_page", 10)
    theme = req_data.get("theme", "basic")
    domain = req_data.get("domain", "")

    if settings:
        settings.blog_title = blog_title
        settings.blog_desc = blog_desc
        settings.post_per_page = post_per_page
        settings.theme = theme
        settings.domain = domain
    else:
        settings = Settings(
            blog_title=blog_title,
            blog_desc=blog_desc,
            domain=domain,
            theme=theme,
            post_per_page=post_per_page,
        )
        db.session.add(settings)
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json
