from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.utils.db_init import Base


class Top(Base):
    # top recipes ( или все же сделать топ категории,
    # или просто для них значение top=true????????)
    __tablename__ = 'top'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    recipe = relationship("Recipe", back_populates="images")

    def __repr__(self):
        return '<Top %r>' % self.name
