from mixer.backend.flask import mixer

from meier.models.user import User


def test_insert(session):
    ran_user = mixer.blend(User)
    spec_user = mixer.blend(
        User,
        email="test@test.co.kr",
        password="123",
        user_name="test",
        profile_image="",
        user_desc="test",
        twitter_profile="test",
        facebook_profile=None,
        website=None,
    )

    assert User.query.count() == 2


def test_update(session):
    spec_user = mixer.blend(
        User,
        email="test@test.co.kr",
        password="123",
        user_name="test",
        profile_image="",
        user_desc="test",
        twitter_profile="test",
        facebook_profile=None,
        website=None,
    )

    user = User.query.scalar()
    user.email = "sh84.ahn@gmail.com"
    session.commit()
    user1 = User.query.scalar()
    assert user1.email == "sh84.ahn@gmail.com"


def test_delete(session):
    spec_user = mixer.blend(
        User,
        email="test@test.co.kr",
        password="123",
        user_name="test",
        profile_image="",
        user_desc="test",
        twitter_profile="test",
        facebook_profile=None,
        website=None,
    )
    assert User.query.count() == 1
    session.delete(spec_user)
    session.commit()
    assert User.query.count() == 0
