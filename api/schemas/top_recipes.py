from pydantic import BaseModel

from api.schemas.base_ids import BaseIds
from api.schemas.recipe_items import RecipeShortItem


class TopRecipesGetResponse(BaseModel):
    data: list[RecipeShortItem]


class TopRecipesIds(BaseModel):
    top_recipes: list[BaseIds]


class TopRecipesIdsError(BaseModel):
    top_recipes: list[BaseIds]
