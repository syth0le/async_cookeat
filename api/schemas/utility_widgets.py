from pydantic import BaseModel

from api.schemas.base_ids import BaseIds
from api.schemas.utility_items import SummaryItem, CuisineItem, StepItem, EquipmentItem


class BaseClass(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UtilityIds(BaseModel):
    utility_ids: list[BaseIds]

    class Config:
        orm_mode = True


class UtilityIdsError(BaseClass):
    utility_id: int = None
    status: int


class CategoryGetResponse(BaseClass):
    category_id: int
    image: str
    description: str


class EquipmentGetResponse(BaseClass):
    equipment: list[EquipmentItem]


class NutritionGetResponse(BaseClass):
    nutrition_id: int
    influence: str  # enum
    amount: str  # string ???????? what
    percentOfDailyNeeds: float


class IngredientGetResponse(BaseClass):
    id: int
    ingredient_id: int
    image: str
    nutrition: list[NutritionGetResponse]  # get response or item?????
    possible_units: list[str]


class SummaryGetResponse(BaseModel):
    cooker: str  # do it enum povareshka
    summary: list[SummaryItem]

    class Config:
        orm_mode = True


class CuisineGetResponse(BaseModel):
    cuisine: list[CuisineItem]

    class Config:
        orm_mode = True


class StepsGetResponse(BaseModel):
    steps: list[StepItem]
    hints: list[str]

    class Config:
        orm_mode = True


class TasteGetResponse(BaseModel):
    sweetness: float
    saltiness: float
    sourness: float
    bitterness: float
    savoriness: float
    fattiness: float
    spiciness: float

    class Config:
        orm_mode = True

