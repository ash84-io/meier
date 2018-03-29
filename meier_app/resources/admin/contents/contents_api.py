# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request
from flask_login import login_required
from sqlalchemy import desc

from meier_app.commons.logger import logger
from meier_app.commons.response_data import ResponseData, HttpStatusCode
from meier_app.models.post import Post, PostStatus
from meier_app.resources.admin import base
from meier_app.extensions import db


admin_contents_api = Blueprint('admin_contents_api', __name__, url_prefix='/admin/contents/api')


@admin_contents_api.route('/posts', methods=['GET'])
@login_required
@base.api_exception_handler
def get_contents_posts_api():
    logger.debug(request.args)
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    post_paging_result = _get_post_list_by_status(status=PostStatus.PUBLISH, page=page, per_page=per_page)
    post_list = [post.for_admin for i, post in enumerate(post_paging_result.items)]

    is_result = True if post_paging_result.total > 0 else False
    return ResponseData(code=HttpStatusCode.SUCCESS,
                        data={'contents': post_list, 'pagination':{'page': page, 'totalCount': post_paging_result.total}},
                        result=is_result).json


def _get_post_list_by_status(status: PostStatus=None, page=1, per_page=10):
    qs = Post.query
    if status:
        qs = qs.filter(Post.status == status.value)
    return qs.order_by(desc(Post.in_date)).paginate(page, per_page, error_out=False)


@admin_contents_api.route('/draft', methods=['GET'])
@login_required
@base.api_exception_handler
def get_contents_draft_api():
    logger.debug(request.args)
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    post_paging_result = _get_post_list_by_status(status=PostStatus.DRAFT, page=page, per_page=per_page)
    post_list = [post.for_admin for i, post in enumerate(post_paging_result.items)]
    is_result = True if post_paging_result.total > 0 else False
    return ResponseData(code=HttpStatusCode.SUCCESS,
                        data={'contents': post_list, 'pagination':{'page': page, 'totalCount': post_paging_result.total}},
                        result=is_result).json


@admin_contents_api.route('/posts/<int:post_id>', methods=['DELETE'])
@login_required
@base.api_exception_handler
def delete_contents_posts_api(post_id):
    logger.debug(post_id)
    Post.query.filter(Post.id == post_id).delete()

    # todo : post-tag 연결 끊기
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json