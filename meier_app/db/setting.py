# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, Text

from meier_app.db.base import MixinBase
from meier_app.extensions import db


class Settings(db.Model, MixinBase):
    __tablename__ = 'settings'
    __table_args__ = {'extend_existing': True, "mysql_engine": "InnoDB"}

    blog_title = Column(Text, nullable=False)
    blog_desc = Column(Text, nullable=False)
    post_per_page = db.Column(Integer, default=10)