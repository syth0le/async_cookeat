from sqlalchemy import Column, Integer, String

from api.utils.db_init import Base


class Creators(Base):
    __tablename__ = 'creators'

    id = Column(Integer, primary_key=True),  # creator_id
    name = Column(String, unique=True, nullable=False),
    photo = Column(String, unique=True, nullable=False),
    description = Column(String, unique=True, nullable=False)
