# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask_login import login_required, current_user

from meier_app.commons.logger import logger
from meier_app.models.setting import Settings

admin_contents_view = Blueprint('admin_contents_view', __name__, url_prefix='/admin/contents')


@admin_contents_view.route('/', methods=['GET'])
@login_required
def get_contents_view():

    settings = Settings.query.first()
    logger.debug(current_user)
    return render_template("/admin/contents.j2",
                           title="Contents",
                           blog_title=settings.blog_title,
                           current_user=current_user)

