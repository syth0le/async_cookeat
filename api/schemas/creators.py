from typing import Optional

from pydantic import BaseModel, Field

from api.schemas.base_ids import BaseIds


class CreatorItem(BaseModel):
    name: Optional[str]
    image: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True


class CreatorGetResponse(CreatorItem):
    # id: int = Field(alias='creator_id')
    id: int


class CreatorUpdateRequest(CreatorItem):
    pass


class CreatorsIds(BaseModel):
    creators_ids: list[BaseIds]

    class Config:
        orm_mode = True


class CreatorsIdsError(BaseModel):
    # или все таки id вместо creator_id
    creator_id: int = None
    status: int
    name: str = None

    class Config:
        orm_mode = True


class CreatorsGetResponse(BaseModel):
    data: list[CreatorItem]

    class Config:
        orm_mode = True


class CreatorsPostRequest(BaseModel):
    data: list[CreatorItem]

    class Config:
        orm_mode = True
