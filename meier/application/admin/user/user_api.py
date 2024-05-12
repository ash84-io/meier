from datetime import datetime, timedelta
from urllib.parse import parse_qs, urlparse

import pytz
from flask import Blueprint, g, request

from meier.common.jwt_token import Token, create_token
from meier.common.response_data import Cookie, HttpStatusCode, ResponseData
from meier.extensions import db
from meier.infrastructure.models.settings import Settings
from meier.infrastructure.models.user import User
from meier.application.admin import base
from meier.application.admin.base import login_required_api

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
    settings = Settings.query.first()
    req_data = request.get_json()
    email = req_data.get("email", None)
    password = req_data.get("password", None)

    if email and password:
        user = (
            User.query.filter(User.email == email.strip())
            .filter(User.password == password.strip())
            .scalar()
        )
        if user:
            token = create_token(
                token_info=Token(
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
