# -*- coding:utf-8 -*-
import traceback
from flask import Blueprint, g, request, render_template
from attrdict import AttrDict
from meier_app.db.post import Post

post_list_view = Blueprint('post_list_view', __name__, url_prefix='/')


@post_list_view.route('', methods=['GET'])
def get_post_list_view():
    from sqlalchemy import desc
    # todo : POST-TAG RELATION SHIP
    post_list = Post.query.order_by(desc(Post.in_date)).all() # todo : pagination using settings page_per_post
    return render_template("/blog/post_list.html", post_list=post_list)
