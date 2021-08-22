from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import Column

from auth.utils.db_init import Base


class HealthTable(Base):
    __tablename__ = "health"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(String(50), ForeignKey("users.id"), nullable=False)

    owner = relationship("UserTable", back_populates="health")

    class Config:
        orm_mode = True
