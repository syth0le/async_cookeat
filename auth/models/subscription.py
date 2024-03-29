from enum import Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Enum as pgEnum, Column, Integer, ForeignKey, String, Float, DateTime
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

    id = Column(Integer, primary_key=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    type_subscription = Column(pgEnum(SubType), default="free")
    value = Column(Float, default=0)  # (deneg skolko)
    measure = Column(String(40), default="USD")
    date_purchase = Column(DateTime, nullable=True)
    date_expired = Column(DateTime, nullable=True)

    owner = relationship("User", back_populates="subscriptions")

    class Config:
        orm_mode = True
