from pydantic import BaseModel


class BaseIds(BaseModel):
    id: int

    class Config:
        orm_mode = True
