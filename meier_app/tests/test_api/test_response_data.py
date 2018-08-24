from meier_app.commons.response_data import HttpStatusCode
from meier_app.commons.response_data import ResponseData
from meier_app.commons.response_data import ResponseMeta


def test_response_data_empty():
    response = ResponseData()
    assert response.meta.code == HttpStatusCode.SUCCESS
    assert response.meta.message == "SUCCESS"
    assert response.data == {}


def test_response_data_to_dict():
    pass


def test_response_data_to_json():
     response = ResponseData().json


def test_response_meta():
    meta = ResponseMeta()
    meta.code = HttpStatusCode.SUCCESS
    meta.message = "SUCCESS"

