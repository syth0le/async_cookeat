from pydantic import BaseModel

from api.schemas.recipe_items import RecipePostItem


class RecipesPostRequest(BaseModel):
    data: list[RecipePostItem]

    class Config:
        orm_mode = True
