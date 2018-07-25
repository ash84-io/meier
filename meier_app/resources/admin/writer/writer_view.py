# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask_login import current_user

from meier_app.extensions import cache
from meier_app.models.settings import Settings

admin_writer_view = Blueprint('admin_writer_view', __name__, url_prefix='/admin/writer')


@admin_writer_view.route('/', methods=['GET'])
@cache.cached(timeout=3600)
def get_new_writer_view():
    settings = Settings.query.first()
    return render_template("/admin/writer.j2",
                           title="Writer",
                           blog_title=settings.blog_title,
                           current_user=current_user)

