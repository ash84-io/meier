import pytest
from mixer.backend.flask import mixer

from meier_app.extensions import db
from meier_app.models.user import User
from meier_app.tests.base import BaseTestCase
from meier_app.tests.base import app as test_app
from meier_app.commons.utils import clean_html


class TestCommonUtils(BaseTestCase):

    def test_clean_html(self):
        test1 = clean_html(raw_html='<h1>test</h1>')
        assert test1 == 'test'
        test2 = clean_html(raw_html=None)
        assert test2 == None
        test3 = clean_html(raw_html='<h1><div>test</div></h1>')
        assert test3 == 'test'
