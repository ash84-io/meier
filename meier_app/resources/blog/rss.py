# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import send_from_directory

from meier_app.commons.logger import logger
from meier_app.models.settings import Settings

rss = Blueprint('rss', __name__, url_prefix='/rss')


@rss.route('', methods=['GET'])
def get_rss():
    pass