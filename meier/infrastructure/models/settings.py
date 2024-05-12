from sqlalchemy import Column, Integer, String

from meier.extensions import db
from meier.infrastructure.models.base import MixinBase


class Settings(db.Model, MixinBase):
    __tablename__ = "settings"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    blog_title = Column(String(255), nullable=False)
    blog_desc = Column(String(255), nullable=False)
    post_per_page = db.Column(Integer, default=10)
    theme = db.Column(String(255), nullable=False)
    domain = db.Column(String(255), nullable=False)

    @property
    def for_dict(self):
        return {
            "blog_title": self.blog_title,
            "blog_desc": self.blog_desc,
            "theme": self.theme,
            "post_per_page": self.post_per_page,
            "domain": self.domain,
        }

    def __repr__(self):
        return str(vars(self))
