# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

admin_writer_view = Blueprint('admin_writer_view', __name__, url_prefix='/admin/writer')


from meier_app.commons.logger import logger
from meier_app.models.post import Post, PostVisibility, PostStatus
from meier_app.models.setting import Settings
from sqlalchemy import desc
@admin_writer_view.route('/', methods=['GET'])
def get_writer_view():

    settings = Settings.query.first()
    return render_template("/admin/writer.j2",
                           title="Writer",
                           blog_title=settings.blog_title,
                           user_name=None)

