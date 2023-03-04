import random

from flask import Blueprint, request

from meier.commons.response_data import HttpStatusCode, ResponseData
from meier.models.post import Post, PostStatus, PostVisibility

post_api = Blueprint("post_api", __name__, url_prefix="/api/v1")


@post_api.route("/random-post", methods=["GET"])
def get_random_post_url() -> str:
    public_posts = (
        Post.query.filter(Post.status == PostStatus.PUBLISH.value)
        .filter(Post.is_page.is_(False))
        .filter(Post.visibility == PostVisibility.PUBLIC.value)
    )
    random_posts = public_posts.all()
    random_index = random.randint(0, len(random_posts) - 1)
    return ResponseData(
        code=HttpStatusCode.SUCCESS,
        data={"url": random_posts[random_index].link},
    ).json
