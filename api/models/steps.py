from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Steps(Base):
    __tablename__ = 'steps'

    id = Column(Integer, primary_key=True, unique=True)
    number = Column(Integer, nullable=False)
    step = Column(Text, nullable=False)
    is_hint = Column(Boolean, default=False)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))

    recipe_steps = relationship("Recipe", back_populates="steps")

    def __repr__(self):
        return '<Step %r>' % self.number
