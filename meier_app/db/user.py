# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Integer

from meier_app.db.base import MixinBase
from meier_app.extensions import db


class User(db.Model, MixinBase):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True, "mysql_engine": "InnoDB"}

    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False, index=True)
    user_name = Column(String(20), nullable=False)
    profile_image = Column(String(255), nullable=True)