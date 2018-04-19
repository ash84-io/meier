# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import abort, render_template
from meier_app.commons.logger import logger

from meier_app.models.post import Post, PostStatus, PostVisibility
from meier_app.models.post_tag import PostTag
from meier_app.models.tag import Tag
from meier_app.models.settings import Settings

post_detail_view = Blueprint('post_detail_view', __name__, url_prefix='/posts')


@post_detail_view.route('/<string:post_name>', methods=['GET'])
def get_post_detail_view(post_name: str):
    settings = Settings.query.first()
    post = Post.query \
        .filter(Post.post_name == post_name) \
        .filter(Post.visibility == int(PostVisibility.PUBLIC.value)) \
        .filter(Post.status == int(PostStatus.PUBLISH.value)).scalar()

    if post:
        prev_post = Post.query.filter(Post.id < post.id).order_by(Post.id.desc()).first()
        logger.debug('prev_post.post_id :{}'.format(prev_post.id))
        next_post = Post.query.filter(Post.id > post.id).order_by(Post.id).first()
        tag_id_list = [post_tag.tag_id for post_tag in PostTag.query.filter(PostTag.post_id == post.id).all()]
        tag_list = [tag.tag for tag in Tag.query.filter(Tag.id.in_(tag_id_list)).all()]
        return render_template("/themes/"+settings.theme+"/post_detail.html",
                               settings=settings,
                               prev_post=prev_post.for_detail if prev_post else None,
                               next_post=next_post.for_detail if next_post else None,
                               post=post.for_detail,
                               tag_list=tag_list
                               )
    else:
        abort(404)

