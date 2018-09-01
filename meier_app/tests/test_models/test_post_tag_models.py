from mixer.backend.flask import mixer
from meier_app.tests.conftest import session
from meier_app.models.post_tag import PostTag


def test_insert(session):
    mixer.blend(PostTag)
    mixer.blend(PostTag,
                post_id=1,
                tag_id=2
                )
    session.commit()
    assert PostTag.query.count() == 2


def test_update(session):
    p1 = mixer.blend(PostTag,
                     post_id=1,
                     tag_id=2
                     )
    assert p1.post_id == 1
    assert p1.tag_id == 2

    p1.post_id = 2
    p1.tag_id = 3
    session.commit()
    p = PostTag.query.scalar()
    assert p.post_id == 2
    assert p.tag_id == 3


def test_delete(session):
    p1 = mixer.blend(PostTag,
                     post_id=1,
                     tag_id=2
                     )
    session.delete(p1)
    session.commit()
    assert PostTag.query.count() == 0



