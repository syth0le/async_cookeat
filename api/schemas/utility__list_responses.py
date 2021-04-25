from pydantic import BaseModel
from utility_items import CategoryItem, IngredientItem, NutritionItem, CuisineItem


class CategoriesListGetResponse(BaseModel):
    data: list[CategoryItem]


class IngredientsListGetResponse(BaseModel):
    data: list[IngredientItem]


class NutritionListGetResponse(BaseModel):
    data: list[NutritionItem]


class CuisinesListGetResponse(BaseModel):
    data: list[CuisineItem]
