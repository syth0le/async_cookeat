from sqlalchemy import Column, Integer, String, Enum as PgEnum, Float
from enum import Enum
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Influence(Enum):
    bad = "bad"
    neutral = "neutral"
    good = "good"


class Nutrition(Base):
    __tablename__ = 'nutrition'

    id = Column(Integer, primary_key=True, unique=True)  # nutrition_id
    name = Column(String(50), nullable=False, unique=True)
    amount = Column(String(50), nullable=True)  # сделать int или хранить строку с значением и measure
    influence = Column(PgEnum(Influence))
    percent_of_daily_needs = Column(Float, nullable=True)
    nutrition = relationship("NutritionToIngredient", back_populates="child")

    recipes = relationship("NutritionToRecipe", back_populates="child")

    def __repr__(self):
        return '<Nutrition %r>' % self.name
