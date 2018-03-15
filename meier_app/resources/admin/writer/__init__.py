# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

admin_writer_view = Blueprint('admin_writer_view', __name__, url_prefix='/admin/writer')


@admin_writer_view.route('/', methods=['GET'])
def get_writer_view():
    return render_template("/admin/writer.html")
