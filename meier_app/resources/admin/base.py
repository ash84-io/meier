import traceback
from functools import wraps

from attrdict import AttrDict
from flask import request
from flask import redirect
from flask import g
from meier_app.commons.jwt_token import parse_token
from meier_app.commons.logger import logger
from meier_app.commons.response_data import ResponseData, HttpStatusCode
from meier_app.extensions import db
from meier_app.models.user import User


class UnauthorizedException(Exception):
    pass


def api_exception_handler(func):
    """
    각종 예외에 대한 처리
    :param func: VIEW/API 메소드
    :return: HTTP RESPONSE
    """

    @wraps(func)
    def decorate(*args, **kwargs):
        try:
            logger.debug(request)
            result = func(*args, **kwargs)
        except BaseException:
            logger.exception(traceback.format_exc())
            db.session.rollback()
            return ResponseData(code=HttpStatusCode.INTERNAL_SERVER_ERROR).json
        return result

    return decorate


def login_required_view(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        try:
            token = request.cookies.get("token", None)
            g.current_user = _get_current_usr_from_token(token)
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
            g.current_user = _get_current_usr_from_token(token)
            result = func(*args, **kwargs)
        except UnauthorizedException as e:
            logger.exception(e)
            return ResponseData(code=HttpStatusCode.INTERNAL_SERVER_ERROR).json
        return result
    return decorate


def _get_current_usr_from_token(token: str):
    if token:
        parsed_token = AttrDict(parse_token(token))
        current_user = User.query.filter(User.email == parsed_token.email).scalar()
        if not current_user:
            raise UnauthorizedException()
        return current_user
    else:
        raise UnauthorizedException()
