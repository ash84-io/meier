import os
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from meier_app.app import create_app
from meier_app.extensions import db
from mixer.backend.flask import mixer

import unittest

app = create_app()


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object('meier_app.config.TestingConfig')

        mixer.init_app(app)
        self.client = app.test_client()
        pass
        #db.drop_all()
        #db.create_all()

    def tearDown(self):
        pass
        #db.session.remove()
        #db.drop_all()