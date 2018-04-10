# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from flask import request

from meier_app.commons.logger import logger
from meier_app.models.post import Post, PostVisibility, PostStatus
from meier_app.models.setting import Settings
from sqlalchemy import desc

post_list_view = Blueprint('post_list_view', __name__, url_prefix='/',)


@post_list_view.route('', methods=['GET'])
def get_post_list_view():
    logger.debug(post_list_view.static_folder)
    page = int(request.args.get('page', 1))
    logger.debug(page)
    settings = Settings.query.first()
    post_paging_result = Post.query.filter(Post.status == PostStatus.PUBLISH.value)\
        .filter(Post.visibility == PostVisibility.PUBLIC.value)\
        .order_by(desc(Post.in_date)).paginate(page, settings.post_per_page, error_out=False)

    post_list = [post.for_detail for post in post_paging_result.items]
    logger.debug(post_list)

    # todo : add tags

    return render_template("/themes/" + settings.theme + "/post_list.html",
                           blog_title=settings.blog_title,
                           blog_desc=settings.blog_desc,
                           post_list=post_list,
                           has_next=post_paging_result.has_next,
                           next="?page={}".format(page+1),
                           has_prev=post_paging_result.has_prev,
                           prev="?page={}".format(page-1)
                           )
