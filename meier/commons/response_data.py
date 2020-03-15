from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from flask import jsonify


class HttpStatusCode(Enum):

    SUCCESS = 20000
    INVALID_PARAMETER = 40000
    INVALID_AUTHORIZATION = 40100
    NOT_FOUND = 40400
    INTERNAL_SERVER_ERROR = 50000
    DUP_POST_NAME = 50001


class ResponseBase(object):
    def to_dict(self):
        raise NotImplementedError


@dataclass(frozen=True)
class Cookie:
    key: str
    value: str
    expired_at: datetime


class ResponseData(ResponseBase):
    def __init__(
        self,
        code=HttpStatusCode.SUCCESS,
        data=None,
        cookies: Optional[List[Cookie]] = None,
        **kwargs
    ):
        self.meta = ResponseMeta(code=code)
        self.data = data
        self.dummy_data = kwargs if kwargs else {}
        self.cookies = cookies

    def to_dict(self):
        result = dict()
        result["meta"] = self.meta.__dict__
        result["data"] = self.data if self.data is not None else []
        result.update(self.dummy_data)
        return result

    @property
    def json(self):
        http_status_code = int(str(self.meta.code)[:3])
        if self.cookies:
            res = jsonify(self.to_dict())
            for c in self.cookies:
                res.set_cookie(c.key, c.value, expires=c.expired_at)
            return res
        else:
            return jsonify(self.to_dict()), http_status_code


class ResponseMeta(object):
    code = None
    message = None

    def __init__(self, code=HttpStatusCode.SUCCESS):
        self.code = code.value
        self.message = code.name
