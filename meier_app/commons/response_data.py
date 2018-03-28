# -*- coding:utf-8 -*-
from enum import Enum


class HttpStatusCode(Enum):

    SUCCESS = 20000
    INVALID_PARAMETER = 40000
    INVALID_AUTHORIZATION = 40100
    NOT_FOUND = 40400
    INTERNAL_SERVER_ERROR = 50000


class ResponseBase(object):
    def to_dict(self):
        raise NotImplementedError("Need Implementation")


class ResponseData(ResponseBase):

    def __init__(self, code, data=None, **kwargs):
        self.meta = Meta(code=code)
        self.data = data
        self.dummy_data = kwargs if kwargs else {}

    def to_dict(self):
        result = dict()
        result["meta"] = self.meta.__dict__
        result["data"] = self.data if self.data is not None else []
        result.update(self.dummy_data)
        return result

    @property
    def json(self):
        from flask import jsonify
        http_status_code = int(str(self.meta.code)[:3])
        return jsonify(self.to_dict()), http_status_code


class Meta(object):
    code = None
    message = None

    def __init__(self, code=HttpStatusCode.SUCCESS):
        self.code = code.value
        self.message = code.name