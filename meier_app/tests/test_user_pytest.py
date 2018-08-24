import pytest
from mixer.backend.flask import mixer

from meier_app.models.user import User
from conftest import session


@pytest.fixture(scope='function')
def test_user2(session):
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