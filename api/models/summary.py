from sqlalchemy import Column, Integer, String, ARRAY

from api.utils.db_init import Base


class Summary(Base):
    __tablename__ = 'summaries'

    id = Column(Integer, primary_key=True, unique=True)
    cooker = Column(String(50), nullable=True)
    servings = Column(Integer, nullable=True)
    cooking_time = Column(String(50), nullable=True)
    preparation_time = Column(String(50), nullable=True)
    total_time = Column(String(50), nullable=True)

    # recipe_id relationship
    # ForeignKey

