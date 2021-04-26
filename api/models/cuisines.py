from sqlalchemy import Column, Integer, String

from api.utils.db_init import Base


class Cuisine(Base):
    __tablename__ = 'cuisines'

    # cuisine =

    # def __repr__(self):
    #     return '<Cuisine %r>' % self.name
