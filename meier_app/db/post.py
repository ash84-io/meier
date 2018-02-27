# -*- coding:utf-8 -*-
from enum import Enum

from sqlalchemy import Column, Integer, Text

from meier_app.db.base import MixinBase
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

    post_name = Column(Text, nullable=True, unique=True, default=None)
    title = Column(Text, nullable=False, index=True)
    content = Column(Text, nullable=False)
    visibility = Column(Integer, nullable=False, default=PostVisibility.PRIVATE)
    status = Column(Integer, nullable=False, default=PostStatus.DRAFT)