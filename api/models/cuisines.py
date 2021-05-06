from sqlalchemy import Column, String, Text

from api.utils.db_init import Base


class Cuisine(Base):
    __tablename__ = 'cuisines'

    name = Column(String(50), primary_key=True, unique=True, nullable=False)
    image = Column(String(50), unique=True, nullable=False)
    description = Column(Text, unique=True, nullable=False)

    def __repr__(self):
        return '<Cuisine %r>' % self.name
