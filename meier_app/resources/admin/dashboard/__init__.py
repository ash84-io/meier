# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

from meier_app.commons.logger import logger
from meier_app.models.post import Post, PostVisibility, PostStatus
from meier_app.models.settings import Settings
from sqlalchemy import desc

from flask_login import logout_user, login_required, current_user

admin_dashboard_view = Blueprint('admin_dashboard_view', __name__, url_prefix='/admin/dashboard')


@admin_dashboard_view.route('/', methods=['GET'])
@login_required
def get_dashboard_view():
    settings = Settings.query.first()
    return render_template("/admin/dashboard.j2",
                           title="DashBoard",
                           blog_title=settings.blog_title,
                           user_name=None)
