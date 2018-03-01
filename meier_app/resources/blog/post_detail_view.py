# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import abort

from meier_app.models.post import Post, PostStatus, PostVisibility
from meier_app.models.setting import Settings
from meier_app.resources.blog.helper_render import *

post_detail_view = Blueprint('post_detail_view', __name__, url_prefix='/posts')


@post_detail_view.route('/<string:post_name>', methods=['GET'])
def get_post_detail_view(post_name):
    settings = Settings.query.first()
    post = Post.query \
        .filter(Post.post_name == post_name) \
        .filter(Post.visibility == int(PostVisibility.PUBLIC.value)) \
        .filter(Post.status == int(PostStatus.PUBLISH.value)).scalar()

    if post:
        return render_template("/themes/"+settings.theme+"/post_detail.html",
                               blog_title=settings.blog_title,
                               blog_desc=settings.blog_desc,
                               post=post.for_detail
                               )
    else:
        abort(404)

