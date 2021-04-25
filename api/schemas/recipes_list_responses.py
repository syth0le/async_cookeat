from pydantic import BaseModel

from api.schemas.recipe_items import RecipeLongItem, RecipeShortItem


class RecipesLongListGetResponse(BaseModel):
    data: list[RecipeLongItem]


class RecipesShortListGetResponse(BaseModel):
    data: list[RecipeShortItem]


class RecipesIds:
    recipes: list[
        id: int
    ]


class RecipesIdsError:
    recipes: list[
        id: int
    ]