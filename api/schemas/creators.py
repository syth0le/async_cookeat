from pydantic import BaseModel


class CreatorItem(BaseModel):
    name: str
    image: str
    description: str


class CreatorGetResponse(CreatorItem):
    creator_id: int


class CreatorUpdateRequest(CreatorItem):
    pass


class CreatorsIds(BaseModel):
    creator_id: int


class CreatorsIdsError(CreatorsIds):
    # или все таки id вместо creator_id
    pass


class CreatorsGetResponse(BaseModel):
    data: list[CreatorItem]


class CreatorsPostRequest(BaseModel):
    data: list[CreatorItem]
