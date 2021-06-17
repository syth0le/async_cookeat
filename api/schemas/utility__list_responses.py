from pydantic import BaseModel
from api.schemas.utility_items import CategoryItem, IngredientItem, NutritionItem, CuisineItem


class CategoriesListGetResponse(BaseModel):
    data: list[CategoryItem]

    class Config:
        orm_mode = True


class IngredientsListGetResponse(BaseModel):
    data: list[IngredientItem]

    class Config:
        orm_mode = True


class NutritionListGetResponse(BaseModel):
    data: list[NutritionItem]

    class Config:
        orm_mode = True


class CuisinesListGetResponse(BaseModel):
    data: list[CuisineItem]

    class Config:
        orm_mode = True
