from enum import IntEnum

from sqlalchemy import Boolean, Column, Integer, String, Text

from meier.extensions import db
from meier.models.base import MixinBase


class Notification(db.Model, MixinBase):
    __tablename__ = "notification"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}
    content = Column(Text, nullable=False)
    is_visible = Column(Boolean, default=True)
