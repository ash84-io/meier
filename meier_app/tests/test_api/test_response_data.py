from meier_app.commons.response_data import HttpStatusCode
from meier_app.commons.response_data import ResponseData
from meier_app.commons.response_data import ResponseMeta
import pytest
from ..conftest import flask_app


def test_response_data_empty():
    response = ResponseData()
    assert response.meta.code == HttpStatusCode.SUCCESS.value
    assert response.meta.message == "SUCCESS"
    assert response.data is None


def test_response_data_to_dict():
    pass


@pytest.fixture(scope="function")
def test_response_data_to_json(flask_app):
    from flask import Response

    response = ResponseData().json
    assert isinstance(response, Response)


def test_response_meta():
    meta = ResponseMeta()
    meta.code = HttpStatusCode.SUCCESS
    meta.message = "SUCCESS"
