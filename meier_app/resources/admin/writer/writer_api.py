# -*- coding:utf-8 -*-
import traceback
from flask import Blueprint, request
from attrdict import AttrDict
from flask_login import login_required

from datetime import datetime
from meier_app.commons.logger import logger
from meier_app.models.post import Post, PostStatus, PostVisibility
from meier_app.models.post_tag import PostTag
from meier_app.models.tag import Tag
from meier_app.models.setting import Settings

from meier_app.extensions import db
from meier_app.resources.admin import base
from meier_app.commons.response_data import ResponseData, HttpStatusCode

admin_writer_api = Blueprint('admin_writer_api', __name__, url_prefix='/admin/writer/api')


@admin_writer_api.route('/post/<int:post_id>', methods=['DELETE'])
@login_required
@base.api_exception_handler
def delete_post(post_id):
    Post.query(Post.id == post_id).delete()
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json


@admin_writer_api.route('/post/<int:post_id>', methods=['PUT'])
@login_required
@base.api_exception_handler
def update_post(post_id):
    req_data = AttrDict(request.get_json())
    post = Post.query(Post.id == post_id).scalar()
    if post:
        for k, v in req_data.items():
            setattr(post, k, v)
        post.mo_date = datetime.now()
        db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json


@admin_writer_api.route('/post', methods=['POST'])
@login_required
@base.api_exception_handler
def save_post():
    req_data = AttrDict(request.get_json())
    post = Post()
    # TODO : MARKDOWN TO HTML CONVERSION
    for k, v in req_data.items():
        setattr(post, k, v)
    post.in_date = datetime.now()
    db.session.add(post)
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json
