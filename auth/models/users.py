from fastapi_users.db import SQLAlchemyBaseUserTable

from auth.utils.db_init import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    __tablename__ = "users"

    class Config:
        orm_mode = True