# -*- coding:utf-8 -*-
from flask import Blueprint, render_template

from meier_app.models.post import Post
from meier_app.models.setting import Settings

post_list_view = Blueprint('post_list_view', __name__, url_prefix='/')


@post_list_view.route('', methods=['GET'])
def get_post_list_view():
    from sqlalchemy import desc

    settings = Settings.query.first()
    # todo : POST-TAG RELATION SHIP
    post_list = [post.for_detail for post in Post.query.order_by(desc(Post.in_date)).all()] # todo : pagination using settings page_per_post
    # todo : settings 를 처음에 로딩시 app.config 에 넣어 두던지 해야할듯.

    return render_template("/themes/" + settings.theme + "/post_list.html",
                           blog_title=settings.blog_title,
                           blog_desc=settings.blog_desc,
                           post_list=post_list
                           )