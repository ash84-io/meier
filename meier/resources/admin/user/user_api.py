from urllib.parse import parse_qs, urlparse

from attrdict import AttrDict
from flask import Blueprint, g, request

from meier.commons.jwt_token import TokenInfo, create_token
from meier.commons.logger import logger
from meier.commons.response_data import HttpStatusCode, ResponseData
from meier.extensions import db
from meier.models.settings import Settings
from meier.models.user import User
from meier.resources.admin import base
from meier.resources.admin.base import login_required_api

admin_user_api = Blueprint(
    "admin_user_api", __name__, url_prefix="/admin/user/api"
)


@admin_user_api.route("/user_info", methods=["GET"])
@login_required_api
@base.api_exception_handler
def user_info_api():
    user = User.query.filter(User.email == g.current_user.email).scalar()
    if not user:
        raise Exception("user_info is none.")
    return ResponseData(
        code=HttpStatusCode.SUCCESS, data=user.for_user_info
    ).json


@admin_user_api.route("/user_info", methods=["PUT"])
@login_required_api
@base.api_exception_handler
def update_user_info_api():
    logger.debug(request.headers)
    logger.debug(request.get_json())
    User.query.filter(User.email == g.current_user.email).update(
        request.get_json()
    )
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json


@admin_user_api.route("/login", methods=["POST"])
@base.api_exception_handler
def login_api():
    logger.debug(request.referrer)
    req_data = AttrDict(request.get_json())
    logger.debug(req_data)
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
            logger.debug("LOGIN_SUCCESS NEXT:{}".format(redirect_url))
            res = ResponseData(
                code=HttpStatusCode.SUCCESS,
                data={"next": redirect_url},
                cookies={"token": token.decode("utf-8")},
            ).json
            return res
        else:
            return ResponseData(code=HttpStatusCode.INVALID_AUTHORIZATION).json
    else:
        return ResponseData(code=HttpStatusCode.INVALID_AUTHORIZATION).json
