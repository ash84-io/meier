from sqlalchemy import Boolean, Column, Text

from meier.extensions import db
from meier.infrastructure.models.base import MixinBase


class Notification(db.Model, MixinBase):
    __tablename__ = "notification"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    content = Column(Text, nullable=False)
    is_visible = Column(Boolean, default=True)
