# -*- coding:utf-8 -*-

from mixer.backend.flask import mixer
import unittest

from meier_app.app import create_app
from meier_app.extensions import db

app = create_app('meier_app.config.TestingConfig')


class BaseAppTestCase(unittest.TestCase):

    def setUp(self): 
        mixer.init_app(app)
        app.config['TESTING'] = True
        self.client = app.test_client()
        db.drop_all(app=app)
        db.create_all(app=app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=app)


class BaseModelTestCase(unittest.TestCase):

    def test_insert(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass
