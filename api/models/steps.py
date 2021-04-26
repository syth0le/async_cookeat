from sqlalchemy import Column, Integer, String, ARRAY

from api.utils.db_init import Base


class Step(Base):
    __tablename__ = 'steps'

    # steps
    hints = Column(ARRAY, nullable=True)

    # def __repr__(self):
    #     return '<Step %r>' % self.name
