# -*- coding:utf-8 -*-
from autorepr import autotext
from sqlalchemy import Column, String

from meier_app.extensions import db
from meier_app.models.base import MixinBase


class User(db.Model, MixinBase):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False, index=True)
    user_name = Column(String(20), nullable=False)
    profile_image = Column(String(255), nullable=True)
    user_desc = db.Column(String(255), nullable=True)
    twitter_profile = db.Column(String(255), nullable=True)
    facebook_profile = db.Column(String(255), nullable=True)
    website = db.Column(String(255), nullable=True)

    __str__, __unicode__ = autotext(
        "{self.email} {self.user_name} {self.profile_image}"
    )

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def for_user_info(self):
        return {
            "email": self.email,
            "user_name": self.user_name,
            "profile_image": self.profile_image,
            "user_desc": self.user_desc,
            "twitter_profile": self.twitter_profile,
            "facebook_profile": self.facebook_profile,
            "website": self.website,
        }

