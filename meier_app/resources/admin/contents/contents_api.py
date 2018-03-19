# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request
from flask_login import login_required
from sqlalchemy import desc
from meier_app.commons.response_data import ResponseData, HttpStatusCode

from meier_app.commons.logger import logger
from meier_app.models.post import Post, PostVisibility, PostStatus

admin_contents_api = Blueprint('admin_contents_api', __name__, url_prefix='/admin/contents/api')


@admin_contents_api.route('/posts', methods=['GET'])
@login_required
def get_contents_posts_api():
    logger.debug(request.args)
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    post_paging_result = Post.query.filter(Post.status == PostStatus.PUBLISH.value).order_by(desc(Post.in_date)).paginate(page, per_page, error_out=False)
    post_list = [post.for_admin for i, post in enumerate(post_paging_result.items)]

    logger.debug(len(post_list))
    for post in post_list:
        logger.debug(post['title'])

    return ResponseData(code=HttpStatusCode.SUCCESS, data={'items':post_list, 'page':page, 'total': post_paging_result.total}).json


@admin_contents_api.route('/draft', methods=['GET'])
@login_required
def get_contents_draft_api():
    logger.debug(request.args)
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    post_paging_result = Post.query.filter(Post.status == PostStatus.DRAFT.value).order_by(desc(Post.in_date)).paginate(page, per_page, error_out=False)
    post_list = [post.for_admin for i, post in enumerate(post_paging_result.items)]

    logger.debug(len(post_list))
    for post in post_list:
        logger.debug(post['title'])

    return ResponseData(code=HttpStatusCode.SUCCESS, data={'items':post_list, 'page':page, 'total': post_paging_result.total}).json
