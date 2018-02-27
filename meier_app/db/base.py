# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, DateTime


class MixinBase(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    in_date = Column(DateTime, index=True)
    mo_date = Column(DateTime, index=True)
