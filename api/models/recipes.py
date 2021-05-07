import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False, unique=True)
    slug = Column(String(256), unique=True)
    is_top_recipe = Column(Boolean, default=False)
    date = Column(DateTime(timezone=True), default=datetime.time)  # переделать

    # category = relationship("Category", backref="recipe", cascade="all, delete-orphan")
    category = Column(String, ForeignKey('categories.name'))
    # cuisine = relationship("Cuisine", backref="recipe", cascade="all, delete-orphan")
    cuisine = Column(String, ForeignKey('cuisines.name'))
    # equipments = relationship("Equipment", backref="recipe", cascade="all, delete-orphan")

    steps = relationship("Steps", back_populates="recipe", cascade="all, delete-orphan")
    images = relationship("Images", back_populates="recipe", cascade="all, delete-orphan")
    summary = relationship("Summary", back_populates="recipe", cascade="all, delete-orphan")
    # nutrition = relationship("Nutrition", back_populates="recipe", cascade="all, delete-orphan")
    # ingredients = relationship("Ingredients", back_populates="recipe", cascade="all, delete-orphan")
    nutrition = relationship("NutritionToRecipe", back_populates="parent")
    equipments = relationship("EquipmentToRecipe", back_populates="parent")
    ingredients = relationship("IngredientToRecipe", back_populates="parent")

# решить где каскадное удаление, а где всенет
# решить и проверить все правильности связок на др таблицы
    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Recipe %r>' % self.name
