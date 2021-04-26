from sqlalchemy import Column, Integer, String, Text
from api.utils.db_init import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, unique=True)  # category_id
    name = Column(String(50), nullable=False, unique=True)
    image = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)

    def __repr__(self):
        return '<Category %r>' % self.name
