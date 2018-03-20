# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask_login import current_user

from meier_app.models.setting import Settings
from meier_app.models.post import Post, PostStatus, PostVisibility

admin_writer_view = Blueprint('admin_writer_view', __name__, url_prefix='/admin/writer')


@admin_writer_view.route('/', methods=['GET'])
def get_new_writer_view():
    settings = Settings.query.first()
    return render_template("/admin/writer.j2",
                           title="Writer",
                           blog_title=settings.blog_title,
                           current_user=current_user)


@admin_writer_view.route('/<post_id:int>', methods=['GET'])
def get_modify_writer_view(post_id):
    settings = Settings.query.first()
    post = Post.query.filter(Post.id == post_id).scalar()
    if post:
        # TODO : IMPLEMENTATION
        pass
    return render_template("/admin/writer.j2",
                           title="Writer",
                           blog_title=settings.blog_title,
                           current_user=current_user)