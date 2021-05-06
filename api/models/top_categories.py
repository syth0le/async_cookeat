from sqlalchemy import Column, Integer, String, ARRAY

from api.utils.db_init import Base


class Top(Base):
    __tablename__ = 'top'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    child = relationship("Category", uselist=False, backref="top")

    def __repr__(self):
        return '<Top %r>' % self.name
