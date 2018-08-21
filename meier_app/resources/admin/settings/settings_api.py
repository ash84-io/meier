# -*- coding:utf-8 -*-
from attrdict import AttrDict
from flask import Blueprint, request
from flask_login import login_required

from meier_app.commons.response_data import ResponseData, HttpStatusCode
from meier_app.extensions import cache
from meier_app.extensions import db
from meier_app.models.settings import Settings
from meier_app.resources.admin import base

admin_settings_api = Blueprint('admin_settings_api', __name__, url_prefix='/admin/settings/api')


@admin_settings_api.route('/blog_info', methods=['GET'])
@cache.cached(timeout=3600)
@login_required
@base.api_exception_handler
def get_settings_blog_info():
    settings = Settings.query.first()
    return ResponseData(code=HttpStatusCode.SUCCESS, data=settings.for_dict).json


@admin_settings_api.route('/blog_info', methods=['POST'])
@login_required
@base.api_exception_handler
def set_settings_blog_info():
    req_data = AttrDict(request.get_json())
    settings = Settings.query.first()
    if settings:
        settings.blog_title = req_data.get('blog_title', '')
        settings.blog_desc = req_data.get('blog_desc', '')
        settings.post_per_page = req_data.get('post_per_page', 10)
        settings.theme = req_data.get('theme', 'basic')
    else:
        settings = Settings(blog_title=req_data.get('blog_title', ''),
                            blog_desc=req_data.get('blog_desc', ''),
                            post_per_page=req_data.get('post_per_page', 10),
                            theme=req_data.get('theme', 'basic'))
        db.session.add(settings)
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json



