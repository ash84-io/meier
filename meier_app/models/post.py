# -*- coding:utf-8 -*-
from enum import Enum

from sqlalchemy import Column, Integer, Text, String, Boolean

from meier_app.models.base import MixinBase
from meier_app.extensions import db


class PostVisibility(Enum):
    PRIVATE = 0
    PUBLIC = 1


class PostStatus(Enum):
    DRAFT = 0
    PUBLISH = 1


class Post(db.Model, MixinBase):
    __tablename__ = 'post'
    __table_args__ = {'extend_existing': True, "mysql_engine": "InnoDB"}
    post_name = Column(String(255), nullable=True, unique=True, default=None)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    html = Column(Text, nullable=True, default=None)
    is_page = Column(Boolean, default=False, index=True)
    visibility = Column(Integer, nullable=False, default=PostVisibility.PRIVATE.value)
    status = Column(Integer, nullable=False, default=PostStatus.DRAFT.value)
    # todo : covered/featured image 추가 여부 고민해보자

    @property
    def for_detail(self):
        return {
            'title': self.title,
            'content': self.content,
            'html': self.html,
            'created_at': self.in_date.strftime("%Y-%m-%d") if self.in_date else '',
            'modified_at': self.mo_date.strftime("%Y-%m-%d") if self.mo_date else '',
            'link': "/posts/" + self.post_name if self.post_name else ''
        }

    @property
    def for_admin(self):
        return {
            'id': self.id,
            'title': self.title,
            'raw_content': self.content,
            'created_at': self.in_date.strftime("%Y-%m-%d") if self.in_date else '',
            'modified_at': self.mo_date.strftime("%Y-%m-%d") if self.mo_date else '',
            'post_name': self.post_name,
            'visibility': self.visibility,
            'status': self.status
        }