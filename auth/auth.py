from datetime import datetime

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from auth.models import UserTable
from auth.schemas.users import UserDB
from auth.utils.db_init import SECRET, database, Base, engine
from auth.schemas.users import *


jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="auth/jwt/login"
)



users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

Base.metadata.create_all(bind=engine)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,)
