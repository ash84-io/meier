import pytest
from mixer.backend.flask import mixer

from meier_app.extensions import db
from meier_app.models.post import Post
from meier_app.tests.base import BaseModelTestCase
from meier_app.tests.base import app as mock_app


class TestPostModels(BaseModelTestCase):

    def test_insert(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass

