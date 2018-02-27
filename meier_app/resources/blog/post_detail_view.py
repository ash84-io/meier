# -*- coding:utf-8 -*-
import traceback
from flask import Blueprint, g, request, render_template
from attrdict import AttrDict

post_detail_view = Blueprint('post_detail_view', __name__, url_prefix='/posts')


@post_detail_view.route('/<string:post_id>', methods=['GET'])
def get_post_detail_view():
    pass
