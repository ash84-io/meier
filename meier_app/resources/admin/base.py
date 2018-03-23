import traceback
from functools import wraps

from flask import request

from meier_app.commons.logger import logger
from meier_app.commons.response_data import ResponseData, HttpStatusCode
from meier_app.extensions import db


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