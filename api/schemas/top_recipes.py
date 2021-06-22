from pydantic import BaseModel

from api.schemas.base_ids import BaseIds
from api.schemas.recipe_items import RecipeShortItem


class TopRecipesGetResponse(BaseModel):
    data: list[RecipeShortItem]


class TopRecipesIds(BaseModel):
    top_recipes_ids: list[BaseIds]


class TopRecipesIdsError(BaseModel):
    recipe_id: int = None
    status: int
    name: str = None

    class Config:
        orm_mode = True
