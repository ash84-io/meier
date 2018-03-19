# -*- coding:utf-8 -*-
from autorepr import autotext
from flask_login import UserMixin
from sqlalchemy import Column, String

from meier_app.extensions import db
from meier_app.models.base import MixinBase


class User(db.Model, MixinBase, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True, "mysql_engine": "InnoDB"}

    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False, index=True)
    user_name = Column(String(20), nullable=False)
    profile_image = Column(String(255), nullable=True)

    __str__, __unicode__ = autotext("{self.email} {self.user_name} {self.profile_image}")

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_id(self):
        return self.token


    @staticmethod
    def get_from_token(token):

        from meier_app.commons.jwt_token import parse_token
        from meier_app.commons.logger import logger
        from attrdict import AttrDict

        logger.debug('get_from_token : {}'.format(token))
        try:
            token_info = AttrDict(parse_token(token))
            user = User(email=token_info.get('email', None),
                        user_name=token_info.get('user_name', None),
                        profile_image=token_info.get('profile_image', None)
                        )
            return user
        except Exception as e:
            logger.exception(e)
            return None
