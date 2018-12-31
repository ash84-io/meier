# -*- coding:utf-8 -*-
from meier_app.extensions import db
from sqlalchemy import Column, Integer, DateTime


class MixinBase(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    in_date = Column(DateTime, index=True, default=db.func.now())
    mo_date = Column(
        DateTime, index=True, default=db.func.now(), onupdate=db.func.now()
    )
