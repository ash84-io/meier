# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask import request, make_response
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from meier_app.commons.logger import logger
from meier_app.models.settings import Settings
from meier_app.models.user import User

admin_contents_view = Blueprint('admin_contents_view', __name__, url_prefix='/admin/contents')


@admin_contents_view.route('/', methods=['GET'])
@jwt_required
def get_contents_view():
    logger.info(request.args)
    settings = Settings.query.first()
    user = User.query.filter(User.email == get_jwt_identity()).scalar()
    resp = make_response(render_template("/admin/contents.j2",
                                         title="Contents", 
                                         blog_title=settings.blog_title,
                                         current_user=user))
    return resp
