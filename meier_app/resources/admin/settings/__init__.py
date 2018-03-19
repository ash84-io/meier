# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

admin_settings_view = Blueprint('admin_settings_view', __name__, url_prefix='/admin/settings')

from meier_app.commons.logger import logger
from meier_app.models.post import Post, PostVisibility, PostStatus
from meier_app.models.setting import Settings
from sqlalchemy import desc
from flask_login import logout_user, login_required, current_user

@admin_settings_view.route('/', methods=['GET'])
@login_required
def get_settings_view():

    settings = Settings.query.first()
    return render_template("/admin/settings.j2",
                           title="Settings",
                           blog_title=settings.blog_title,
                           user_name=None)

