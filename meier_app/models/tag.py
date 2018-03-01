# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String

from meier_app.models.base import MixinBase
from meier_app.extensions import db


class Tag(db.Model, MixinBase):
    __tablename__ = 'tag'
    __table_args__ = {'extend_existing': True, "mysql_engine": "InnoDB"}

    tag = Column(String(255), nullable=False, index=True)