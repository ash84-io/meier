# -*- coding:utf-8 -*-
import traceback
from flask import Blueprint, g, request, render_template
from attrdict import AttrDict

post_list_view = Blueprint('post_list_view', __name__, url_prefix='/posts')


@post_list_view.route('', methods=['GET'])
def get_post_list_view():
    pass
