from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Equipment(Base):
    __tablename__ = 'equipment'

    # id = Column(Integer, primary_key=True, unique=True)  # equipment_id
    name = Column(String(50), primary_key=True, nullable=False, unique=True)
    image = Column(String(50), nullable=True)

    recipes = relationship("NutritionToRecipe", back_populates="child")

    def __repr__(self):
        return '<Equipment %r>' % self.name
