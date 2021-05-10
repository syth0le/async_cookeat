from pydantic import BaseModel

from api.schemas.base_ids import BaseIds
from api.schemas.recipe_items import RecipeLongItem, RecipeShortItem


class RecipesLongListGetResponse(BaseModel):
    data: list[RecipeLongItem]


class RecipesShortListGetResponse(BaseModel):
    data: list[RecipeShortItem]


class RecipesIds:
    recipes: list[BaseIds]


class RecipesIdsError:
    recipes: list[BaseIds]
