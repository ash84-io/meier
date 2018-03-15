# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

admin_settings_view = Blueprint('admin_settings_view', __name__, url_prefix='/admin/settings')


@admin_settings_view.route('/', methods=['GET'])
def get_settings_view():
    return render_template("/admin/settings.html")
