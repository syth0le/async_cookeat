from datetime import datetime
from pydantic import BaseModel

from api.schemas.utility_widgets import CategoryGetResponse, CuisineGetResponse, SummaryGetResponse, StepsGetResponse, \
    IngredientGetResponse, NutritionGetResponse, TasteGetResponse, EquipmentGetResponse


class RecipeGetResponse(BaseModel):
    recipe_id: int
    name: str
    image: str
    category: CategoryGetResponse
    cuisine: CuisineGetResponse
    summary: SummaryGetResponse
    date: datetime  # ???????
    steps: StepsGetResponse
    ingredients: IngredientGetResponse
    nutrition: NutritionGetResponse
    taste: TasteGetResponse
    equipment: EquipmentGetResponse
