# -*- coding:utf-8 -*-
from attrdict import AttrDict
from flask import Blueprint
from flask import request
from flask_login import login_user
from urllib.parse import urlparse, parse_qs

from meier_app.commons.jwt_token import TokenInfo, create_token
from meier_app.commons.logger import logger
from meier_app.commons.response_data import ResponseData, HttpStatusCode
from meier_app.models.setting import Settings
from meier_app.models.user import User

admin_user_api = Blueprint('admin_user_api', __name__, url_prefix='/admin/user')


@admin_user_api.route('/login', methods=['POST'])
def login_api():
    logger.debug(request.referrer)
    req_data = AttrDict(request.get_json())
    logger.debug(req_data)
    settings = Settings.query.first()
    if req_data.email and req_data.password:
        user = User.query.filter(User.email == req_data.email.strip()) \
            .filter(User.password == req_data.password.strip()).scalar()
        if user:
            token = create_token(token_info=TokenInfo(
                user_name=user.user_name,
                email=user.email,
                profile_image=user.profile_image,
                blog_title=settings.blog_title if settings else None
            ))

            user.token = token
            login_user(user)
            next = '/admin/contents'
            if request.referrer:
                url_parsed = urlparse(url=request.referrer)
                if url_parsed.query:
                    parsed_qs = parse_qs(url_parsed.query)
                    next = parsed_qs.get('next', ['/admin/contents'])[0]
            return ResponseData(code=HttpStatusCode.SUCCESS, data={'next': next}).json
        else:
            return ResponseData(code=HttpStatusCode.INVALID_AUTHORIZATION).json
    else:
        return ResponseData(code=HttpStatusCode.INVALID_AUTHORIZATION).json
