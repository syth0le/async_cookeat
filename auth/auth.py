import sqlalchemy
from fastapi import APIRouter
from fastapi_users import models
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
import databases
from dotenv import load_dotenv
import os

from sqlalchemy.orm import sessionmaker

load_dotenv(override=True)
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
postgresserver = os.getenv("POSTGRES_DB")

AUTH_DATABASE_URL = f"postgresql://{user}:{password}@localhost:5432/{postgresserver}"

database = databases.Database(AUTH_DATABASE_URL)

Base: DeclarativeMeta = declarative_base()


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


engine = sqlalchemy.create_engine(
    AUTH_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Base.metadata.create_all(engine)

users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)


@router.get("")
async def login():
    return "login"
