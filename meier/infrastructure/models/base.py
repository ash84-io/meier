from sqlalchemy import Column, DateTime, Integer

from meier.extensions import db


class MixinBase(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    in_date = Column(DateTime, index=True, default=db.func.now())
    mo_date = Column(
        DateTime, index=True, default=db.func.now(), onupdate=db.func.now()
    )
