from fastapi import APIRouter

router = APIRouter(
    prefix="/recipes",
    tags=['recipes'],
    responses={404: {"description": "Not found"}}
)


@router.get("")
async def recipes():
    return "/recipes"


@router.get("/{recipe_id}")
async def single_recipe_by_id(recipe_id: int):
    return f"/{recipe_id}"


@router.get("/<str:title>")
async def single_recipe_by_title():
    return "/<str:title>"


@router.get("/top")
async def top_recipes():
    return "/top"


@router.get("/random")
async def random_recipes():
    return "/random"


@router.get("/{recipe_id}/similar")
async def similar_recipes(recipe_id: int):
    return f"/{recipe_id}/similar"


@router.get("/autocomplete")
async def autocomplete_recipes():
    return "/autocomplete"


@router.get("/{recipe_id}/tasteWidget")
async def taste_by_id(recipe_id: int):
    return f"/{recipe_id}/tasteWidget"


@router.get("/{recipe_id}/equipmentWidget")
async def equipment_by_id(recipe_id: int):
    return f"/{recipe_id}/equipmentWidget"


@router.get("/{recipe_id}/ingredientWidget")
async def ingredients_by_id(recipe_id: int):
    return f"/{recipe_id}/ingredientWidget"


@router.get("/{recipe_id}/nutritionWidget")
async def nutrition_by_id(recipe_id: int):
    return f"/{recipe_id}/nutritionWidget"


@router.get("/{recipe_id}/stepsWidget")
async def steps_by_id(recipe_id: int):
    return f"/{recipe_id}/stepsWidget"


@router.get("/{recipe_id}/summaryWidget")
async def summary_by_id(recipe_id: int):
    return f"/{recipe_id}/summaryWidget"


@router.get("/{recipe_id}/cuisineWidget")
async def cuisine_by_id(recipe_id: int):
    return f"/{recipe_id}/cuisineWidget"
