# -*- coding:utf-8 -*-
import traceback

from flask import Blueprint
from flask import render_template, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from meier_app.commons.logger import logger
from meier_app.models.user import User
from meier_app.models.settings import Settings

admin_user_view = Blueprint('admin_user_view', __name__, url_prefix='/admin/user')


@admin_user_view.route('/', methods=['GET'])
@jwt_required
def get_user_view():
    settings = Settings.query.first()
    user = User.query.filter(User.email == get_jwt_identity()).scalar()
    return render_template("/admin/user.j2",
                           title="User",
                           blog_title=settings.blog_title,
                           current_user=user)


@admin_user_view.route('/login', methods=['GET'])
def login_view():
    return render_template("/admin/login.j2")


@admin_user_view.route('/logout', methods=['GET'])
def logout_view():
    try: 
        resp = make_response(render_template("/admin/login.j2"))
        resp.set_cookie('access_token_cookie', '', expires=0)
        return resp
    except BaseException:
        logger.exception(traceback.format_exc())
