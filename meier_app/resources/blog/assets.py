# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import send_from_directory

from meier_app.models.settings import Settings
from meier_app.extensions import cache

assets = Blueprint('assets', __name__, url_prefix='/assets')


@assets.route('/css/<string:file_name>', methods=['GET'])
def get_assets_css_file(file_name: str):
    settings = Settings.query.first()
    return response_assets(theme=settings.theme, static_folder='css', file_name=file_name)


@assets.route('/js/<string:file_name>', methods=['GET'])
def get_assets_js_file(file_name: str):
    settings = Settings.query.first()
    return response_assets(theme=settings.theme, static_folder='js', file_name=file_name)


@assets.route('/img/<string:file_name>', methods=['GET'])
def get_assets_img_file(file_name: str):
    settings = Settings.query.first()
    return response_assets(theme=settings.theme, static_folder='img', file_name=file_name)


@assets.route('/font/<string:file_name>', methods=['GET'])
def get_assets_font_file(file_name: str):
    settings = Settings.query.first()
    return response_assets(theme=settings.theme, static_folder='font', file_name=file_name)


def response_assets(theme, static_folder, file_name):
    return send_from_directory('templates/themes/{}/assets/{}/'.format(theme, static_folder), file_name)

