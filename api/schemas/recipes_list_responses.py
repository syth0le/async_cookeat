from pydantic import BaseModel

from api.schemas.base_ids import BaseIds
from api.schemas.recipe_items import RecipeLongItem, RecipeShortItem


class RecipesLongListGetResponse(BaseModel):
    data: list[RecipeLongItem]


class RecipesShortListGetResponse(BaseModel):
    data: list[RecipeShortItem]


class RecipesIds(BaseModel):
    recipes_ids: list[BaseIds]


class RecipesIdsError(BaseModel):
    recipe_id: int = None
    status: int
    name: str = None

    class Config:
        orm_mode = True
