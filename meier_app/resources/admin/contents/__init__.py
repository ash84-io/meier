# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

admin_contents_view = Blueprint('admin_contents_view', __name__, url_prefix='/admin/contents')


@admin_contents_view.route('/', methods=['GET'])
def get_contents_view():
    return render_template("/admin/contents.html")
