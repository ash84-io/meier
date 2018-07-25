# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from flask import request
from sqlalchemy import desc

from meier_app.models.post import Post, PostVisibility, PostStatus
from meier_app.models.settings import Settings
from meier_app.models.user import User
from meier_app.resources.blog.meta_tag.og_meta_tag import OpenGraphMetaTagGenerator
from meier_app.extensions import cache

post_list_view = Blueprint('post_list_view', __name__, url_prefix='/',)


@post_list_view.route('/', methods=['GET'])
@cache.cached(timeout=300)
def get_post_list_view():
    author = User.query.first()
    page = int(request.args.get('page', 1))
    settings = Settings.query.first()
    post_paging_result = Post.query.filter(Post.status == PostStatus.PUBLISH.value) \
        .filter(Post.is_page.is_(False)) \
        .filter(Post.visibility == PostVisibility.PUBLIC.value) \
        .order_by(desc(Post.in_date)).paginate(page, settings.post_per_page, error_out=False)

    post_list = [post.for_detail for post in post_paging_result.items]
    first_post = post_list[0]
    ogp_meta_tag = OpenGraphMetaTagGenerator(site_name=settings.blog_title,
                                             title=first_post.get('title', None),
                                             description=first_post.get('content', None)[:300],
                                             url=first_post.get('link', None),
                                             image=first_post.get('featured_image', None)
                                             )

    return render_template("/themes/" + settings.theme + "/post_list.html",
                           author=author,
                           ogp_meta_tag=ogp_meta_tag(),
                           settings=settings,
                           total_pages=post_paging_result.pages,
                           post_list=post_list,
                           has_next=post_paging_result.has_next,
                           next="?page={}".format(page+1),
                           has_prev=post_paging_result.has_prev,
                           prev="?page={}".format(page-1)
                           )
