from datetime import datetime, timedelta
from urllib.parse import parse_qs, urlparse

import pytz
from attrdict import AttrDict
from flask import Blueprint, g, request

from meier.commons.jwt_token import TokenInfo, create_token
from meier.commons.response_data import Cookie, HttpStatusCode, ResponseData
from meier.extensions import db
from meier.models.settings import Settings
from meier.models.user import User
from meier.views.admin import base
from meier.views.admin.base import login_required_api

KST = pytz.timezone("Asia/Seoul")


admin_user_api = Blueprint(
    "admin_user_api", __name__, url_prefix="/admin/user/api"
)


@admin_user_api.route("/user_info", methods=["GET"])
@login_required_api
@base.exc_handler
def user_info_api():
    user = User.query.filter(User.email == g.current_user.email).scalar()
    if not user:
        raise Exception("user_info is none.")
    return ResponseData(
        code=HttpStatusCode.SUCCESS, data=user.for_user_info
    ).json


@admin_user_api.route("/user_info", methods=["PUT"])
@login_required_api
@base.exc_handler
def update_user_info_api():
    User.query.filter(User.email == g.current_user.email).update(
        request.get_json()
    )
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json


@admin_user_api.route("/login", methods=["POST"])
@base.exc_handler
def login_api():
    req_data = AttrDict(request.get_json())
    settings = Settings.query.first()
    if req_data.email and req_data.password:
        user = (
            User.query.filter(User.email == req_data.email.strip())
            .filter(User.password == req_data.password.strip())
            .scalar()
        )
        if user:
            token = create_token(
                token_info=TokenInfo(
                    user_name=user.user_name,
                    email=user.email,
                    profile_image=user.profile_image,
                    blog_title=settings.blog_title if settings else None,
                )
            )

            redirect_url = "/admin/contents"
            if request.referrer:
                url_parsed = urlparse(url=request.referrer)
                if url_parsed.query:
                    parsed_qs = parse_qs(url_parsed.query)
                    redirect_url = parsed_qs.get("next", ["/admin/contents"])[
                        0
                    ]
            expired_at = datetime.now(tz=KST) + timedelta(minutes=30)
            print(token)
            res = ResponseData(
                code=HttpStatusCode.SUCCESS,
                data={"next": redirect_url},
                cookies=[Cookie("token", token, expired_at)],
            ).json
            return res
        else:
            return ResponseData(code=HttpStatusCode.INVALID_AUTHORIZATION).json
    else:
        return ResponseData(code=HttpStatusCode.INVALID_AUTHORIZATION).json
