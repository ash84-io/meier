from flask import Blueprint, render_template, request
from sqlalchemy import desc

from meier.models.post import Post, PostStatus, PostVisibility
from meier.models.post_tag import PostTag
from meier.models.settings import Settings
from meier.models.tag import Tag
from meier.models.user import User
from meier.views.blog.services.open_graph import OpenGraphMetaTagGenerator

tag_list_view = Blueprint("tag_list_view", __name__, url_prefix="/tag")


@tag_list_view.route("/<string:tag>", methods=["GET"])
@tag_list_view.route("/<string:tag>/", methods=["GET"])
def get_tag_list_view(tag: str):
    author = User.query.first()
    page = int(request.args.get("page", 1))
    settings = Settings.query.first()

    tag = Tag.query.filter(Tag.tag == tag).scalar()
    if tag:
        post_tag_list = PostTag.query.filter(PostTag.tag_id == tag.id).all()
        post_id_list = [post_tag.post_id for post_tag in post_tag_list]
        post_paging_result = (
            Post.query.filter(Post.status == PostStatus.PUBLISH.value)
            .filter(Post.is_page.is_(False))
            .filter(Post.id.in_(post_id_list))
            .filter(Post.visibility == PostVisibility.PUBLIC.value)
            .order_by(desc(Post.in_date))
            .paginate(page, settings.post_per_page, error_out=False)
        )

        post_list = [post.for_detail for post in post_paging_result.items]
        has_next = post_paging_result.has_next
        has_prev = post_paging_result.has_prev
        next = "?page={}".format(page + 1)
        prev = "?page={}".format(page - 1)
        total_pages = post_paging_result.pages
    else:
        post_list = []
        has_next = None
        has_prev = None
        next = None
        prev = None
        total_pages = 0
    ogp_meta_tag = OpenGraphMetaTagGenerator(
        site_name=settings.blog_title,
        title=settings.blog_title,
        description=settings.blog_desc,
        url=settings.domain,
        image=None,
    )
    return render_template(
        f"/themes/{settings.theme}/post_list.html",
        author=author,
        ogp_meta_tag=ogp_meta_tag(),
        settings=settings,
        total_pages=total_pages,
        post_list=post_list,
        has_next=has_next,
        next=next,
        has_prev=has_prev,
        prev=prev,
    )
