# -*- coding:utf-8 -*-
import traceback
from flask import Blueprint, g, request, render_template
from attrdict import AttrDict
from meier_app.models.post import Post
from meier_app.models.setting import Settings
from meier_app.commons.logger import logger
from meier_app.resources.blog.helper_render import *

post_list_view = Blueprint('post_list_view', __name__, url_prefix='/')


@post_list_view.route('', methods=['GET'])
def get_post_list_view():
    from sqlalchemy import desc

    settings = Settings.query.first()
    # todo : POST-TAG RELATION SHIP
    post_list = Post.query.order_by(desc(Post.in_date)).all() # todo : pagination using settings page_per_post
    # todo : settings 를 처음에 로딩시 app.config 에 넣어 두던지 해야할듯.
    return render_template("/themes/"+settings.theme+"/post_list.html",
                           blog_title=blog_title_helper(settings.blog_title),
                           blog_desc=blog_desc_helper(settings.blog_desc),
                           post_list=post_list_helper(post_list))
