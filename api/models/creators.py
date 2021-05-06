from sqlalchemy import Column, Integer, String, Text

from api.utils.db_init import Base


class Creators(Base):
    __tablename__ = 'creators'

    id = Column(Integer, primary_key=True)  # creator_id
    name = Column(String(50), unique=True, nullable=False)
    image = Column(String(50), unique=True, nullable=False)
    description = Column(Text, unique=True, nullable=False)
