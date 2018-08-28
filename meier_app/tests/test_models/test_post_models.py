from mixer.backend.flask import mixer
from meier_app.tests.conftest import session

from meier_app.models.post import Post, PostStatus, PostVisibility


def test_insert(session):
    p1 = mixer.blend(Post)
    p2 = mixer.blend(Post,
                     post_name="test",
                     title="test",
                     content="test",
                     html="test",
                     is_page=False,
                     visibility=PostVisibility.PUBLIC,
                     status=PostStatus.DRAFT,
                     featured_image="test"
                     )

    assert p2.post_name == 'test'
    assert p2.title == 'test'
    assert p2.content == 'test'
    assert p2.html == 'test'
    assert p2.visibility == PostVisibility.PUBLIC
    assert p2.status == PostStatus.DRAFT
    assert p2.featured_image == "test"
    assert Post.query.count() == 2

    for_detail_keys = {'title': str,
                       'content': str,
                       'html': str,
                       'created_at': str,
                       'modified_at': str,
                       'link': str,
                       'featured_image': str,
                       'is_page': bool}

    for k, v in p2.for_detail.items():
        assert isinstance(v, for_detail_keys[k])

    for_admin_keys = {
        'id': int,
        'raw_content': str,
        'post_name': str,
        'title': str,
        'content': str,
        'html': str,
        'created_at': str,
        'modified_at': str,
        'link': str,
        'featured_image': str,
        'is_page': bool
    }

    for k, v in p2.for_admin.items():
        assert isinstance(v, for_admin_keys[k])


def test_update(session):
    mixer.blend(Post)

    p = Post.query.scalar()
    p.post_name = "blog"
    p.title = "blog"
    p.post_name = 'blog'
    p.title = 'blog'
    p.content = 'blog'
    p.html = 'blog'
    p.visibility = PostVisibility.PRIVATE
    p.status = PostStatus.PUBLISH
    p.featured_image = "blog"

    session.commit()
    assert p.post_name == 'blog'
    assert p.title == 'blog'
    assert p.content == 'blog'
    assert p.html == 'blog'
    assert p.visibility == PostVisibility.PRIVATE
    assert p.status == PostStatus.PUBLISH
    assert p.featured_image == "blog"
 

def test_delete(session):
    mixer.blend(Post)
    p = Post.query.scalar()
    session.delete(p)
    session.commit()
    assert Post.query.count() == 0

