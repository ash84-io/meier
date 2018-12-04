# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from meier_app.models.settings import Settings
from meier_app.extensions import cache

admin_dashboard_view = Blueprint('admin_dashboard_view', __name__, url_prefix='/admin/dashboard')


@admin_dashboard_view.route('/', methods=['GET'])
@cache.cached(timeout=86400)
def get_dashboard_view():
    settings = Settings.query.first()
    return render_template("/admin/dashboard.j2",
                           title="DashBoard",
                           blog_title=settings.blog_title,
                           user_name=None)
