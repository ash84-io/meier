from sqlalchemy import Column, Integer

from meier.extensions import db
from meier.models.base import MixinBase


class PostTag(db.Model, MixinBase):
    __tablename__ = "post_tag"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    tag_id = Column(Integer, nullable=False, index=True)
    post_id = Column(Integer, nullable=False, index=True)
