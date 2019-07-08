from sqlalchemy import Column, String

from meier.extensions import db
from meier.models.base import MixinBase


class Tag(db.Model, MixinBase):
    __tablename__ = "tag"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    tag = Column(String(255), nullable=False, index=True)

    @property
    def for_admin(self):
        return self.tag
