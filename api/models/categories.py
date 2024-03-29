from sqlalchemy import Column, Boolean, String, Text
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Category(Base):
    __tablename__ = 'categories'

    # id = Column(Integer, primary_key=True, unique=True)  # category_id
    name = Column(String(50), primary_key=True, unique=True, default=None)
    image = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    is_top_category = Column(Boolean, default=False)

    recipes = relationship("Recipe")

    def __repr__(self):
        return '<Category %r>' % self.name

# подумать чтобы сделать back_populates здесь и в категориях чтобы по ним получать все рецепты(хз)
