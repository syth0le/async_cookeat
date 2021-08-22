from enum import Enum
from sqlalchemy import Enum as pgEnum, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from auth.utils.db_init import Base


class SubType(Enum):
    free = "free"
    month = "month"
    half_year = "half_year"
    year = "year"
    all_time = "all_time"


class SubscriptionTable(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(String(50), ForeignKey("users.id"), nullable=False, primary_key=True)
    type_subscription = Column(pgEnum(SubType), default=False)
    # value(deneg skolko)
    # amount(value)
    # date_expired
    # date_purchase

    owner = relationship("User", back_populates="subscriptions")

    class Config:
        orm_mode = True
