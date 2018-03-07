# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from flask import request

from meier_app.commons.logger import logger
from meier_app.models.post import Post, PostVisibility, PostStatus
from meier_app.models.setting import Settings

post_list_view = Blueprint('post_list_view', __name__, url_prefix='/')


@post_list_view.route('', methods=['GET'])
def get_post_list_view():
    page = request.args.get('page', 1)
    from sqlalchemy import desc

    settings = Settings.query.first()
    post_result = Post.query.filter(Post.status == PostStatus.PUBLISH.value)\
        .filter(Post.visibility == PostVisibility.PUBLIC.value)\
        .order_by(desc(Post.in_date)).paginate(page, settings.post_per_page, error_out=False)

    post_list = [post.for_detail for post in post_result.items]

    # todo : pagination using settings page_per_post
    # todo : settings 를 처음에 로딩시 app.config 에 넣어 두던지 해야할듯.

    return render_template("/themes/" + settings.theme + "/post_list.html",
                           blog_title=settings.blog_title,
                           blog_desc=settings.blog_desc,
                           post_list=post_list
                           )