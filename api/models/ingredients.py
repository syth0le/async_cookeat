from sqlalchemy import Column, Integer, String, ARRAY

from api.utils.db_init import Base


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, unique=True)  # ingredient_id
    name = Column(String(50), nullable=False, unique=True)
    image = Column(String(50), nullable=False, unique=True)
    # nutrition = relationship Nutrition
    possible_units = Column(ARRAY, nullable=False)

    def __repr__(self):
        return '<Ingredient %r>' % self.name
