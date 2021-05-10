from pydantic import BaseModel


class BaseClass(BaseModel):
    name: str


class CategoryItem(BaseClass):
    category_id: int
    image: str
    description: str


class NutritionItem(BaseClass):
    nutrition_id: int
    influence: str  # enum


class IngredientItem(BaseClass):
    ingredient_id: int
    image: str
    nutrition: list[NutritionItem]
    possible_units: list[str]
    category_path: list[str]


class CuisineItem(BaseClass):
    cuisine_id: int
    description: str


class EquipmentItem(BaseClass):
    equipment_id: int
    image: str


class StepItem(BaseClass):
    step_id: int
    number: int
    step: str
    is_hint: bool


class SummaryItem(BaseClass):
    summary_id: int
    measure: str
    quantity: int
