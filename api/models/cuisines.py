from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Cuisine(Base):
    __tablename__ = 'cuisines'

    name = Column(String(50), primary_key=True, unique=True, default=None)
    image = Column(String(50), unique=True, nullable=False)
    description = Column(Text, unique=True, nullable=False)

    recipes = relationship("Recipe")

    def __repr__(self):
        return '<Cuisine %r>' % self.name

# подумать чтобы сделать back_populates здесь и в категориях чтобы по ним получать все рецепты(хз)