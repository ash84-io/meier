from functools import wraps

from flask import g, redirect, request

from meier.common.jwt_token import parse_token
from meier.common.logger import logger
from meier.common.response_data import HttpStatusCode, ResponseData
from meier.extensions import db
from meier.infrastructure.models.user import User


class UnauthorizedException(Exception):
    pass


def exc_handler(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
            return ResponseData(code=HttpStatusCode.INTERNAL_SERVER_ERROR).json
        return result

    return decorate


def login_required_view(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        try:
            token = request.cookies.get("token", None)
            g.current_user = get_current_user_from_token(token)
            result = func(*args, **kwargs)
        except UnauthorizedException as e:
            logger.exception(e)
            return redirect("/admin/user/login", code=302)
        return result

    return decorate


def login_required_api(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        try:
            token = request.cookies.get("token", None)
            g.current_user = get_current_user_from_token(token)
            result = func(*args, **kwargs)
        except UnauthorizedException as e:
            logger.exception(e)
            return ResponseData(code=HttpStatusCode.INTERNAL_SERVER_ERROR).json
        return result

    return decorate


def get_current_user_from_token(token: str):
    if not token:
        raise UnauthorizedException

    parsed_token = parse_token(token)
    current_user = User.query.filter(
        User.email == parsed_token["email"]
    ).scalar()
    if not current_user:
        raise UnauthorizedException
    return current_user
