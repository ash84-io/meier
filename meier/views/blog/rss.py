from datetime import timezone

from feedgen.feed import FeedGenerator
from flask import Blueprint, Response
from sqlalchemy import desc

from meier.models.post import Post, PostStatus, PostVisibility
from meier.models.post_tag import PostTag
from meier.models.settings import Settings
from meier.models.tag import Tag
from meier.models.user import User

rss = Blueprint("rss", __name__, url_prefix="")


@rss.route("/rss/", methods=["GET"])
@rss.route("/rss", methods=["GET"])
def get_rss():
    settings = Settings.query.first()
    author = User.query.first()
    fg = FeedGenerator()
    fg.title(settings.blog_title)
    fg.author({"name": author.user_name, "email": author.email})
    fg.link(href=settings.domain, rel="alternate")
    fg.description(description=settings.blog_desc)
    post_paging_result = (
        Post.query.filter(Post.status == PostStatus.PUBLISH.value)
        .filter(Post.is_page.is_(False))
        .filter(Post.visibility == PostVisibility.PUBLIC.value)
        .order_by(desc(Post.in_date))
        .limit(15)
        .all()
    )

    post_paging_result = reversed(post_paging_result)
    for post in post_paging_result:
        tag_id_list = [
            post_tag.tag_id
            for post_tag in PostTag.query.filter(
                PostTag.post_id == post.id
            ).all()
        ]
        tag_list = [
            tag.tag for tag in Tag.query.filter(Tag.id.in_(tag_id_list)).all()
        ]
        post_path = post.for_detail['link']
        fe = fg.add_entry()
        fe.author({"name": author.user_name, "email": author.email})
        categories = [
            {"term": tag, "scheme": None, "label": tag} for tag in tag_list
        ]
        fe.category(categories)
        fe.title(post.title)
        fe.description(description="<![CDATA[ {} ]]>".format(post.html[:200]))
        fe.content(content=post.html, type="CDATA")
        fe.link(href=f"{settings.domain}/{post_path}", rel="alternate")
        fe.pubdate(str(post.in_date.astimezone(timezone.utc)))
        fe.id(post.post_name)

    rss_feed = fg.rss_str(pretty=True)
    return Response(rss_feed, mimetype="text/xml")
