import datetime

from pydantic import BaseModel

from api.schemas.utility_widgets import CategoryGetResponse, CuisineGetResponse, SummaryGetResponse, StepsGetResponse, \
    IngredientGetResponse, NutritionGetResponse, TasteGetResponse, EquipmentGetResponse


class RecipeShortItem(BaseModel):
    recipe_id: int
    name: str
    image: str
    category: CategoryGetResponse
    cuisine: CuisineGetResponse
    summary: SummaryGetResponse

    # __example__ = {
    #     "name": "Foo",
    #     "category": "A very nice Item"
    # }


class RecipeLongItem(RecipeShortItem):
    date: datetime.datetime  # ???????
    steps: StepsGetResponse
    ingredients: IngredientGetResponse
    nutrition: NutritionGetResponse
    taste: TasteGetResponse
    equipment: EquipmentGetResponse


class RecipePostItem(BaseModel):
    name: str
    slug: str
    # images: str # ImagesResponse
    # category: CategoryGetResponse
    # cuisine: CuisineGetResponse
    # summary: SummaryGetResponse
    # date: datetime.datetime  # ???????
    # steps: StepsGetResponse
    # ingredients: IngredientGetResponse
    # nutrition: NutritionGetResponse
    # taste: TasteGetResponse
    # equipment: EquipmentGetResponse
