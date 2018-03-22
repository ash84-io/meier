# -*- coding:utf-8 -*-
from flask import Blueprint, request
from attrdict import AttrDict
from flask_login import login_required

admin_writer_api = Blueprint('admin_writer_api', __name__, url_prefix='/admin/writer/api')


@admin_writer_api.route('/post/<int:post_id>', methods=['DELETE'])
@login_required
def delete_post(post_id):
    pass


@admin_writer_api.route('/post/<int:post_id>', methods=['PUT'])
@login_required
def update_post(post_id):
    req_data = AttrDict(request.get_json())
    pass


@admin_writer_api.route('/post', methods=['POST'])
@login_required
def save_post():
    req_data = AttrDict(request.get_json())
    pass