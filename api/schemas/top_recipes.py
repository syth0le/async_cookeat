from pydantic import BaseModel

from api.schemas.recipe_items import RecipeShortItem


class TopRecipesGetResponse(BaseModel):
    data: list[RecipeShortItem]


class TopRecipesIds:
    top_recipes: list[
        id: int
    ]


class TopRecipesIdsError:
    top_recipes: list[
        id: int
    ]
