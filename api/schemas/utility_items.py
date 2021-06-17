from pydantic import BaseModel, Field

from api.models.nutrition import Influence


class BaseClass(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CategoryItem(BaseClass):
    name: str
    image: str
    is_top_category: bool
    description: str


class NutritionItem(BaseClass):
    id: int
    influence: Influence  # enum

    # class Config:
    #     allow_population_by_alias = True
    #     fields = {'id2': 'id'}


class IngredientItem(BaseClass):
    id: int
    image: str
    # nutrition: list[NutritionItem]
    possible_units: list[str]
    # category_path: list[str]


class CuisineItem(BaseClass):
    image: str
    description: str


class EquipmentItem(BaseClass):
    id: int
    image: str


class StepItem(BaseClass):
    id: int
    number: int
    step: str
    is_hint: bool


class SummaryItem(BaseClass):
    id: int
    measure: str
    quantity: int
