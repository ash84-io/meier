import pytest
from mixer.backend.flask import mixer

from meier_app.extensions import db
from meier_app.models.user import User
from meier_app.tests.base import BaseModelTestCase
from meier_app.tests.base import app as mock_app


class TestUserModels(BaseModelTestCase):

    def test_insert(self):
        with mock_app.app_context():
            ran_user = mixer.blend(User)
            spec_user = mixer.blend(User,
                                    email='test@test.co.kr',
                                    password='123',
                                    user_name='test',
                                    profile_image="",
                                    user_desc="test",
                                    twitter_profile="test",
                                    facebook_profile=None,
                                    website=None)

            assert User.query.count() == 2

    def test_update(self):
        with mock_app.app_context():
            spec_user = mixer.blend(User,
                                    email='test@test.co.kr',
                                    password='123',
                                    user_name='test',
                                    profile_image="",
                                    user_desc="test",
                                    twitter_profile="test",
                                    facebook_profile=None,
                                    website=None)

            user = User.query.scalar()
            user.email = "sh84.ahn@gmail.com"
            db.session.commit()
            user1 = User.query.scalar()
            assert user1.email == 'sh84.ahn@gmail.com'

    def test_delete(self):
        with mock_app.app_context():
            spec_user = mixer.blend(User,
                                    email='test@test.co.kr',
                                    password='123',
                                    user_name='test',
                                    profile_image="",
                                    user_desc="test",
                                    twitter_profile="test",
                                    facebook_profile=None,
                                    website=None)
            assert User.query.count() == 1
            db.session.delete(spec_user)
            db.session.commit()
            assert User.query.count() == 0

    def test_unique_email(self):
        from sqlalchemy import exc
        with mock_app.app_context():
            try:
                spec_user = mixer.blend(User,
                                        email='test@test.co.kr')
                spec_user = mixer.blend(User,
                                        email='test@test.co.kr')

            except exc.IntegrityError:
                db.session.rollback()


