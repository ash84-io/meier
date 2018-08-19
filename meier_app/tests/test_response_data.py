from meier_app.commons.response_data import ResponseData
from meier_app.commons.response_data import HttpStatusCode
from meier_app.commons.response_data import ResponseBase
from meier_app.commons.response_data import ResponseMeta
from meier_app.tests.base import BaseTestCase


class TestResponseData(BaseTestCase):
    def setUp(self):
        pass

    def test_response_data_empty(self):
        response = ResponseData()
        assert response.meta.code == HttpStatusCode.SUCCESS
        assert response.meta.message == "SUCCESS"
        assert response.data == {}

    def test_response_data_to_dict(self):
        pass

    def test_response_data_to_json(self):
         response = ResponseData().json

    def test_response_meta(self):
        meta = ResponseMeta()
        meta.code = HttpStatusCode.SUCCESS
        meta.message = "SUCCESS"

