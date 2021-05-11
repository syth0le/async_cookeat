from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False, unique=True)
    slug = Column(String(256), unique=True)
    is_top_recipe = Column(Boolean, default=False)
    created_date = Column(DateTime(timezone=True), default=func.now())

    sweetness = Column(Float)
    saltiness = Column(Float)
    sourness = Column(Float)
    bitterness = Column(Float)
    savoriness = Column(Float)
    fattiness = Column(Float)
    spiciness = Column(Float)

    category = Column(String, ForeignKey('categories.name'))
    cuisine = Column(String, ForeignKey('cuisines.name'))

    steps = relationship("Steps", back_populates="recipe_steps", cascade="all, delete-orphan")
    images = relationship("Images", back_populates="recipe_image", cascade="all, delete-orphan")
    summary = relationship("Summary", back_populates="recipe_summary", cascade="all, delete-orphan")
    nutrition = relationship("NutritionToRecipe", back_populates="parent_nutrition", cascade="all, delete-orphan")
    equipments = relationship("EquipmentToRecipe", back_populates="parent_equipments", cascade="all, delete-orphan")
    ingredients = relationship("IngredientToRecipe", back_populates="parent_ingredients", cascade="all, delete-orphan")

# решить где каскадное удаление, а где всенет
# решить и проверить все правильности связок на др таблицы
    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Recipe %r>' % self.name
