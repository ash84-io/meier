# -*- coding:utf-8 -*-

from sqlalchemy import Column, String

from meier_app.extensions import db
from meier_app.models.base import MixinBase


class Tag(db.Model, MixinBase):
    __tablename__ = "tag"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    tag = Column(String(255), nullable=False, index=True)

    def __init__(self, tag):
        self.tag = tag

    @property
    def for_admin(self):
        return self.tag
