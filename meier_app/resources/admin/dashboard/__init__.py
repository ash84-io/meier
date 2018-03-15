# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

admin_dashboard_view = Blueprint('admin_dashboard_view', __name__, url_prefix='/admin')


@admin_dashboard_view.route('/dashboard', methods=['GET'])
def get_dashboard_view():
    return render_template("/admin/dashboard.j2", title="DashBoard")
