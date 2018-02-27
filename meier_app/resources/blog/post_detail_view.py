# -*- coding:utf-8 -*-
import traceback
from flask import Blueprint, g, request, render_template
from attrdict import AttrDict
from meier_app.db.post import Post

post_detail_view = Blueprint('post_detail_view', __name__, url_prefix='/posts')


@post_detail_view.route('/<string:post_name>', methods=['GET'])
def get_post_detail_view(post_name):
    post = Post.query.filter(Post.post_name == post_name).scalar()
    return render_template("/blog/post_detail.html", post=post)

