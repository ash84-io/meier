# -*- coding:utf-8 -*-
from flask import Blueprint, redirect
admin_index_view = Blueprint('admin_index_view', __name__, url_prefix='/admin')


@admin_index_view.route('', methods=['GET'])
def get_index_view():
        return redirect("/admin/contents", code=302)