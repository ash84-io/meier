# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request
from sqlalchemy import desc
from sqlalchemy import or_

from flask_jwt_extended import jwt_required
from meier_app.commons.logger import logger
from meier_app.commons.response_data import ResponseData, HttpStatusCode
from meier_app.extensions import db
from meier_app.models.post import Post, PostStatus
from meier_app.models.post_tag import PostTag
from meier_app.models.tag import Tag
from meier_app.resources.admin import base

admin_contents_api = Blueprint('admin_contents_api', __name__, url_prefix='/admin/contents/api')


@admin_contents_api.route('/posts', methods=['GET'])
@jwt_required
@base.api_exception_handler
def get_contents_posts_api():
    logger.debug(request.args)
    q = request.args.get('q', None)
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    post_paging_result = _get_post_list_by_status(status=PostStatus.PUBLISH, page=page, per_page=per_page, q=q)
    post_list = [post.for_admin for i, post in enumerate(post_paging_result.items)]

    is_result = True if post_paging_result.total > 0 else False
    return ResponseData(code=HttpStatusCode.SUCCESS,
                        data={'contents': post_list,
                              'pagination': {'page': page, 'totalCount': post_paging_result.total}},
                        result=is_result).json


def _get_post_list_by_status(status: PostStatus=None, page=1, per_page=10, q=None):
    qs = Post.query
    if status:
        qs = qs.filter(Post.status == status.value)
    if q:
        q_str = '%{}%'.format(q)
        qs = qs.filter(or_(Post.title.like(q_str), Post.post_name.like(q_str)))
    return qs.order_by(desc(Post.in_date)).paginate(page, per_page, error_out=False)


@admin_contents_api.route('/draft', methods=['GET'])
@jwt_required
@base.api_exception_handler
def get_contents_draft_api():
    logger.debug(request.args)
    q = request.args.get('q', None)
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    post_paging_result = _get_post_list_by_status(status=PostStatus.DRAFT, page=page, per_page=per_page, q=q)
    post_list = [post.for_admin for i, post in enumerate(post_paging_result.items)]
    is_result = True if post_paging_result.total > 0 else False
    return ResponseData(code=HttpStatusCode.SUCCESS,
                        data={'contents': post_list,
                              'pagination': {'page': page, 'totalCount': post_paging_result.total}},
                        result=is_result).json


@admin_contents_api.route('/posts/<int:post_id>', methods=['DELETE'])
@jwt_required
@base.api_exception_handler
def delete_contents_posts_api(post_id):
    logger.debug(post_id)
    Post.query.filter(Post.id == post_id).delete()
    PostTag.query.filter(PostTag.post_id == post_id).delete()
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json


@admin_contents_api.route('/posts/<int:post_id>', methods=['GET'])
@jwt_required
@base.api_exception_handler
def get_contents_post_detail_api(post_id):
    logger.debug(request.args)
    post = Post.query.filter(Post.id == int(post_id)).scalar()
    tag_id_list = [pt.tag_id for pt in PostTag.query.filter(PostTag.post_id == int(post_id)).all()]
    tags = ','.join([t.for_admin for t in Tag.query.filter(Tag.id.in_(tag_id_list)).all()])
    if not post:
        return ResponseData(code=HttpStatusCode.NOT_FOUND).json
    return ResponseData(code=HttpStatusCode.SUCCESS,
                        data={'post': post.for_admin, 'tags': tags}
                        ).json
