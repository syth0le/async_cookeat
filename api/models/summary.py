from sqlalchemy import Column, Integer, String, ARRAY

from api.utils.db_init import Base


class Summary(Base):
    __tablename__ = 'summaries'

    cooker = Column(String(50), nullable=True)
    # summary

    # def __repr__(self):
    #     return '<Summary %r>' % self.name
