# -*- coding:utf-8 -*-
import traceback

from flask import Blueprint
from flask import render_template
from flask_login import logout_user, login_required, current_user

from meier_app.commons.logger import logger
from meier_app.models.settings import Settings
from meier_app.models.user import User

admin_user_view = Blueprint('admin_user_view', __name__, url_prefix='/admin/user')


@admin_user_view.route('/', methods=['GET'])
@login_required
def get_user_view():
    settings = Settings.query.first()
    return render_template("/admin/user.j2",
                           title="User",
                           blog_title=settings.blog_title,
                           current_user=current_user)


@admin_user_view.route('/login', methods=['GET'])
def login_view():
    return render_template("/admin/login.j2")


@admin_user_view.route('/logout', methods=['GET'])
def logout_view():
    try:
        logout_user()
        return render_template("/admin/login.j2")
    except BaseException:
        # TODO : TEST
        logger.exception(traceback.format_exc())
