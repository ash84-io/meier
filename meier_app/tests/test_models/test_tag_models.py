from mixer.backend.flask import mixer

from meier_app.models.tag import Tag 
from meier_app.tests.conftest import session


def test_insert(session):
    mixer.blend(Tag)
    mixer.blend(Tag, tag='test')
    assert Tag.query.count() == 2


def test_update(session):
    spec_tag = mixer.blend(Tag, tag='test')
    spec_tag.tag = "test123"
    session.commit()
    t = Tag.query.scalar()
    assert t.tag == "test123"


def test_delete(session):
    mixer.blend(Tag)
    spec_tag = mixer.blend(Tag, tag='test')
    session.delete(spec_tag)
    session.commit()
    assert Tag.query.count() == 1

