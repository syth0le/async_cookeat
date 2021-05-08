from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Summary(Base):
    __tablename__ = 'summary'

    id = Column(Integer, primary_key=True, unique=True)
    cooker = Column(String(50), nullable=True)
    servings = Column(Integer, nullable=True)
    cooking_time = Column(String(50), nullable=True)
    preparation_time = Column(String(50), nullable=True)
    total_time = Column(String(50), nullable=True)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))

    recipe_summary = relationship("Recipe", back_populates="summary")
