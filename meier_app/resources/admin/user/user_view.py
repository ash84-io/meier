# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from meier_app.commons.logger import logger
from meier_app.models.post import Post, PostVisibility, PostStatus
from meier_app.models.setting import Settings
from sqlalchemy import desc
import traceback
from flask_login import logout_user, login_required, current_user

admin_user_view = Blueprint('admin_user_view', __name__, url_prefix='/admin/user')


@admin_user_view.route('/', methods=['GET'])
@login_required
def get_user_view():

    settings = Settings.query.first()
    return render_template("/admin/user.j2",
                           title="User",
                           blog_title=settings.blog_title,
                           user_name=None)


@admin_user_view.route('/login', methods=['GET'])
def login_view():
    return render_template("/admin/login.j2")


@admin_user_view.route('/logout', methods=['GET'])
def logout_view():
    try:
        logout_user()
        logger.debug("로그아웃")
        return render_template("/admin/login.j2")
    except BaseException:
        logger.exception(traceback.format_exc())
