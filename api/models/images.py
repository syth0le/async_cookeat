from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Images(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, unique=True)
    # recipe_id = Column(Integer, ForeignKey('recipes.id'))
    image = Column(String(50), nullable=False)

    # recipe relationship

    def __repr__(self):
        return '<Images %r>' % self.image
