from pydantic import BaseModel

from api.schemas.recipe_items import RecipeShortItem


class TopRecipesGetResponse(BaseModel):
    data: list[RecipeShortItem]


class TopRecipesIds(BaseModel):
    # smt: str
    top_recipes: list[int]


# class TopRecipesIdsError(BaseModel):
#     top_recipes: list[
#         id: int
#     ]
