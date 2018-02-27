# -*- coding:utf-8 -*-
from autorepr import autotext
from sqlalchemy import Column, String, Integer

from meier_app.db.base import MixinBase
from meier_app.extensions import db


class User(db.Model, MixinBase):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True, "mysql_engine": "InnoDB"}

    seqno = db.Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True, index=True, default=None, doc="이메일")
    password = Column(String(255), nullable=False, index=True, default=None, doc="이메일")
    user_name = Column(String(20), nullable=False, doc="대화명")
    profile = Column(String(255), nullable=True, doc="프로필사진")

    __str__, __unicode__ = autotext("{self.email}")