from typing import Optional

from fastapi_users import models


class User(models.BaseUser):
    name: str
    lastname: str
    phone: str
    age: Optional[int]
    weight: Optional[float]
    height: Optional[float]
    is_have_subscription: Optional[bool]
    is_paid: Optional[bool]
    value_paid: Optional[float]
    measure: Optional[float]
    is_shared: Optional[bool]


class UserCreate(models.BaseUserCreate):
    name: str
    lastname: str
    phone: str
    age: Optional[int]
    weight: Optional[float]
    height: Optional[float]
    is_have_subscription: Optional[bool]
    is_paid: Optional[bool]
    value_paid: Optional[float]
    measure: Optional[float]
    is_shared: Optional[bool]


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
