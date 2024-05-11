from flask import Blueprint, abort, render_template
from flask import g, request

from meier.admin.base import get_current_user_from_token, UnauthorizedException
from meier.blog.services.opengraph import OpenGraphMetaTagGenerator
from meier.models.post import Post, PostStatus, PostVisibility
from meier.models.post_tag import PostTag
from meier.models.settings import Settings
from meier.models.tag import Tag
from meier.models.user import User

post_detail_view = Blueprint("post_detail_view", __name__, url_prefix="")


@post_detail_view.route(
    "/<int:yyyy>/<string:mm>/<string:dd>/<string:post_name>/", methods=["GET"]
)
def get_post_detail_view(yyyy: int, mm: str, dd: str, post_name: str):

    token = request.cookies.get("token", None)
    try:
        current_user = get_current_user_from_token(token)
    except UnauthorizedException:
        current_user = None

    settings = Settings.query.first()
    author = User.query.first()

    post = (
        Post.query.filter(Post.post_name == post_name)
        .filter(Post.visibility == PostVisibility.PUBLIC.value)
        .filter(Post.status == PostStatus.PUBLISH.value)
        .scalar()
    )

    if not post:
        abort(404)

    prev_post = (
        Post.query.filter(Post.id < post.id)
        .filter(Post.visibility == PostVisibility.PUBLIC.value)
        .filter(Post.status == PostStatus.PUBLISH.value)
        .order_by(Post.id.desc())
        .first()
    )
    next_post = (
        Post.query.filter(Post.id > post.id)
        .filter(Post.visibility == PostVisibility.PUBLIC.value)
        .filter(Post.status == PostStatus.PUBLISH.value)
        .order_by(Post.id)
        .first()
    )
    tag_id_list = [
        post_tag.tag_id
        for post_tag in PostTag.query.filter(PostTag.post_id == post.id).all()
    ]

    tag_list = [
        tag.tag for tag in Tag.query.filter(Tag.id.in_(tag_id_list)).all()
    ]

    ogp_meta_tag = OpenGraphMetaTagGenerator(
        site_name=settings.blog_title,
        title=post.for_detail.get("title", None),
        description=post.for_detail.get("content", None)[:300],
        url=post.for_detail.get("link", None),
        image=post.for_detail.get("featured_image", None),
    )

    related_post_tags = (
        PostTag.query.filter(PostTag.tag_id.in_(tag_id_list))
        .order_by(PostTag.id.desc())
        .limit(10)
        .all()
    )
    related_post_ids = [
        related_post_tag.post_id for related_post_tag in related_post_tags
    ]

    try:
        related_post_ids.remove(post.id)
        related_post = (
            Post.query.filter(Post.id == related_post_ids[0]).first()
            if related_post_ids
            else None
        )
    except ValueError:
        related_post = None

    return render_template(
        f"themes/{settings.theme}/post_detail.html",
        author=author,
        current_user=current_user,
        ogp_meta_tag=ogp_meta_tag(),
        settings=settings,
        prev_post=prev_post.for_detail if prev_post else None,
        next_post=next_post.for_detail if next_post else None,
        post=post.for_detail,
        tag_list=tag_list,
        related_post=related_post.for_detail if related_post else None,
    )
