from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True, unique=True)  # ingredient_id
    name = Column(String(50), nullable=False, unique=True)
    image = Column(String(50), nullable=False, unique=True)
    possible_units = Column(ARRAY(String), nullable=False)
    nutrition = relationship("NutritionToIngredient", back_populates="parent")
    # написать проверку в процентах от 0 до 100
    recipes = relationship("IngredientToRecipe", back_populates="child")

    def __repr__(self):
        return '<Ingredient %r>' % self.name
