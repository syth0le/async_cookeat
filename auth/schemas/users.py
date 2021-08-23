from typing import Optional

from fastapi_users import models
from pydantic import EmailStr


class User(models.BaseUser):
    #response after creating and verify and me and update
    name: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    age: Optional[int]
    weight: Optional[float]
    height: Optional[float]
    is_have_subscription: Optional[bool] = False
    is_paid: Optional[bool] = False
    value_paid: Optional[float]
    measure: Optional[str]
    is_shared: Optional[bool] = False


class UserCreate(models.BaseUserCreate):
    name: str
    lastname: Optional[str]
    phone: Optional[str]
    age: Optional[int]
    weight: Optional[float]
    height: Optional[float]
    is_have_subscription: Optional[bool] = False
    is_paid: Optional[bool] = False
    value_paid: Optional[float] = 0
    measure: Optional[str] = "USD"
    is_shared: Optional[bool] = False


class UserUpdate(User, models.BaseUserUpdate):
    # request update
    pass


class UserDB(User, models.BaseUserDB):
    pass
