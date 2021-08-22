from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, String, Integer, Float
from sqlalchemy.orm import relationship

from auth.utils.db_init import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    __tablename__ = "users"

    name = Column(String(50))
    lastname = Column(String(50))
    phone = Column(String(50))
    age = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)

    is_have_subscription = Column(Boolean, default=False) # est' li podpiska
    is_paid = Column(Boolean, default=False) # zaplatil li za podpisku
    value_paid = Column(Float, nullable=False) # skolko zaplatil za podpisku
    is_shared = Column(Boolean, default=False) # (podelilsya li s drugom)

    # health = relationship("SubscriptionTable", back_populates="owner") # ossobennosty zdorovya
    # subscriptions = relationship("HealthTable", back_populates="owner")

    class Config:
        orm_mode = True
