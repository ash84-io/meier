# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

admin_account_view = Blueprint('admin_account_view', __name__, url_prefix='/admin/account')


@admin_account_view.route('/', methods=['GET'])
def get_account_view():
    return render_template("/admin/account.html")
