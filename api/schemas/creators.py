from pydantic import BaseModel, Field


class CreatorItem(BaseModel):
    name: str
    image: str
    description: str

    class Config:
        orm_mode = True


class CreatorGetResponse(CreatorItem):
    # id: int = Field(alias='creator_id')
    id: int


class CreatorUpdateRequest(CreatorItem):
    pass


class CreatorsIds(BaseModel):
    creator_id: int

    class Config:
        orm_mode = True


class CreatorsIdsError(CreatorsIds):
    # или все таки id вместо creator_id
    pass


class CreatorsGetResponse(BaseModel):
    data: list[CreatorItem]

    class Config:
        orm_mode = True


class CreatorsPostRequest(BaseModel):
    data: list[CreatorItem]

    class Config:
        orm_mode = True
