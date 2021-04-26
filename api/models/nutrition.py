from sqlalchemy import Column, Integer, String, Enum as PgEnum, Float
from enum import Enum

from api.utils.db_init import Base


class Influence(Enum):
    bad = "bad"
    neutral = "neutral"
    good = "good"


class Nutrition(Base):
    __tablename__ = 'nutrition'

    id = Column(Integer, primary_key=True, unique=True)  # nutrition_id
    name = Column(String(50), nullable=False, unique=True)
    amount = Column(String(50), nullable=True)
    influence = Column(PgEnum(Influence))
    percentOfDailyNeeds = Column(Float, nullable=True)

    def __repr__(self):
        return '<Nutrition %r>' % self.name
