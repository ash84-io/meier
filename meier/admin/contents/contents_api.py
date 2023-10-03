from flask import Blueprint, request
from sqlalchemy import desc, or_

from meier.commons.response_data import HttpStatusCode, ResponseData
from meier.extensions import db
from meier.models.post import Post, PostStatus
from meier.models.post_tag import PostTag
from meier.models.tag import Tag
from meier.admin import base
from meier.admin.base import login_required_api

admin_contents_api = Blueprint(
    "admin_contents_api", __name__, url_prefix="/admin/contents/api"
)


@admin_contents_api.route("/posts", methods=["GET"])
@login_required_api
@base.exc_handler
def get_contents_posts_api():
    q = request.args.get("q", None)
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("perPage", 10))

    post_paging_result = _get_post_list_by_status(
        status=PostStatus.PUBLISH, page=page, per_page=per_page, q=q
    )
    post_list = [post.for_admin for post in post_paging_result.items]

    is_result = post_paging_result.total > 0
    return ResponseData(
        code=HttpStatusCode.SUCCESS,
        data={
            "contents": post_list,
            "pagination": {
                "page": page,
                "totalCount": post_paging_result.total,
            },
        },
        result=is_result,
    ).json


def _get_post_list_by_status(
    status: PostStatus = None, page=1, per_page=10, q=None
):
    qs = Post.query
    if status is not None:
        qs = qs.filter(Post.status == status.value)
    if q:
        q_str = f"%{q}%"
        qs = qs.filter(or_(Post.title.like(q_str), Post.post_name.like(q_str)))
    return qs.order_by(desc(Post.in_date)).paginate(
        page, per_page, error_out=False
    )


@admin_contents_api.route("/draft", methods=["GET"])
@login_required_api
@base.exc_handler
def get_contents_draft_api():
    q = request.args.get("q", None)
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("perPage", 10))

    post_paging_result = _get_post_list_by_status(
        status=PostStatus.DRAFT, page=page, per_page=per_page, q=q
    )
    post_list = [post.for_admin for post in post_paging_result.items]
    is_result = post_paging_result.total > 0
    return ResponseData(
        code=HttpStatusCode.SUCCESS,
        data={
            "contents": post_list,
            "pagination": {
                "page": page,
                "totalCount": post_paging_result.total,
            },
        },
        result=is_result,
    ).json


@admin_contents_api.route("/posts/<int:post_id>", methods=["DELETE"])
@login_required_api
@base.exc_handler
def delete_contents_posts_api(post_id):

    Post.query.filter(Post.id == post_id).delete()
    PostTag.query.filter(PostTag.post_id == post_id).delete()
    db.session.commit()
    return ResponseData(code=HttpStatusCode.SUCCESS).json


@admin_contents_api.route("/posts/<int:post_id>", methods=["GET"])
@login_required_api
@base.exc_handler
def get_contents_post_detail_api(post_id):
    post = Post.query.filter(Post.id == int(post_id)).scalar()
    tag_id_list = [
        pt.tag_id
        for pt in PostTag.query.filter(PostTag.post_id == int(post_id)).all()
    ]
    tags = ",".join(
        [t.for_admin for t in Tag.query.filter(Tag.id.in_(tag_id_list)).all()]
    )
    if not post:
        return ResponseData(code=HttpStatusCode.NOT_FOUND).json
    return ResponseData(
        code=HttpStatusCode.SUCCESS,
        data={"post": post.for_admin, "tags": tags},
    ).json
