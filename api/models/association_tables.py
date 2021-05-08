from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class NutritionToRecipe(Base):
    __tablename__ = 'nutrition_a'

    recipe_id = Column(Integer, ForeignKey('recipe.id'), primary_key=True)
    nutrition_id = Column(Integer, ForeignKey('nutrition.id'), primary_key=True)
    extra_data = Column(String(50))
    child = relationship("Nutrition", back_populates="recipes")
    parent_nutrition = relationship("Recipe", back_populates="nutrition")


class EquipmentToRecipe(Base):
    __tablename__ = 'equipment_a'

    recipe_id = Column(Integer, ForeignKey('recipe.id'), primary_key=True)
    equipment_id = Column(String, ForeignKey('equipment.name'), primary_key=True)
    extra_data = Column(String(50))
    child = relationship("Equipment", back_populates="recipes")
    parent_equipments = relationship("Recipe", back_populates="equipments")


class IngredientToRecipe(Base):
    __tablename__ = 'ingredient_a'

    recipe_id = Column(Integer, ForeignKey('recipe.id'), primary_key=True)
    equipment_id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    extra_data = Column(String(50))
    child = relationship("Ingredient", back_populates="recipes")
    parent_ingredients = relationship("Recipe", back_populates="ingredients")


class NutritionToIngredient(Base):
    __tablename__ = 'nutrition_to_recipe_a'

    ingredient_id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    nutrition_id = Column(Integer, ForeignKey('nutrition.id'), primary_key=True)
    extra_data = Column(String(50))
    child = relationship("Nutrition", back_populates="nutrition")
    parent = relationship("Ingredient", back_populates="nutrition")
