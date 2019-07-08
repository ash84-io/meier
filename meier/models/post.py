from enum import IntEnum

from sqlalchemy import Boolean, Column, Integer, String, Text

from meier.extensions import db
from meier.models.base import MixinBase


class PostVisibility(IntEnum):
    PRIVATE = 0
    PUBLIC = 1


class PostStatus(IntEnum):
    DRAFT = 0
    PUBLISH = 1


class Post(db.Model, MixinBase):
    __tablename__ = "post"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}
    post_name = Column(String(255), nullable=True, unique=True, default=None)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    html = Column(Text, nullable=True, default=None)
    is_page = Column(Boolean, default=False, index=True)
    visibility = Column(
        Integer, nullable=False, default=PostVisibility.PRIVATE.value
    )
    status = Column(Integer, nullable=False, default=PostStatus.DRAFT.value)
    featured_image = Column(Text, nullable=True, default=None)

    @property
    def for_detail(self):
        return {
            "title": self.title,
            "content": self.content,
            "html": self.html,
            "created_at": self.in_date.strftime("%Y-%m-%d")
            if self.in_date
            else "",
            "modified_at": self.mo_date.strftime("%Y-%m-%d")
            if self.mo_date
            else "",
            "link": "/{}/{}/{}/".format(
                self.in_date.strftime("%Y"),
                self.in_date.strftime("%m"),
                self.in_date.strftime("%d"),
            )
            + self.post_name
            if self.post_name
            else "",
            "featured_image": self.featured_image,
            "is_page": self.is_page,
        }

    @property
    def for_admin(self):
        return {
            "id": self.id,
            "title": self.title,
            "raw_content": self.content,
            "created_at": self.in_date.strftime("%Y-%m-%d")
            if self.in_date
            else "",
            "modified_at": self.mo_date.strftime("%Y-%m-%d")
            if self.mo_date
            else "",
            "post_name": self.post_name,
            "visibility": self.visibility,
            "status": self.status,
            "featured_image": self.featured_image,
            "is_page": self.is_page,
        }
