from sqlalchemy import ForeignKey, String, Integer, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from auth.utils.db_init import Base


class HealthTable(Base):
    __tablename__ = "health"

    id = Column(Integer, primary_key=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String(50), nullable=False)

    owner = relationship("UserTable", back_populates="health")

    class Config:
        orm_mode = True
