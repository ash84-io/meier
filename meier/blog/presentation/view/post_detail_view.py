from flask import Blueprint, abort, render_template

from meier.models.post import Post, PostStatus, PostVisibility
from meier.models.post_tag import PostTag
from meier.models.settings import Settings
from meier.models.tag import Tag
from meier.models.user import User
from meier.blog.services.opengraph import OpenGraphMetaTagGenerator

post_detail_view = Blueprint("post_detail_view", __name__, url_prefix="")


@post_detail_view.route(
    "/<int:yyyy>/<string:mm>/<string:dd>/<string:post_name>/", methods=["GET"]
)
def get_post_detail_view(yyyy: int, mm: str, dd: str, post_name: str):
    settings = Settings.query.first()
    author = User.query.first()

    post = (
        Post.query.filter(Post.post_name == post_name)
        .filter(Post.visibility == PostVisibility.PUBLIC.value)
        .filter(Post.status == PostStatus.PUBLISH.value)
        .scalar()
    )

    if post:
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
            for post_tag in PostTag.query.filter(
                PostTag.post_id == post.id
            ).all()
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

        return render_template(
            f"themes/{settings.theme}/post_detail.html",
            author=author,
            ogp_meta_tag=ogp_meta_tag(),
            settings=settings,
            prev_post=prev_post.for_detail if prev_post else None,
            next_post=next_post.for_detail if next_post else None,
            post=post.for_detail,
            tag_list=tag_list,
        )
    else:
        abort(404)
