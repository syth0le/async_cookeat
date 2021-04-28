from fastapi import APIRouter

from api.handlers.recipes import get_recipes, post_recipes, get_recipe_by_id, get_recipe_by_title, get_top_recipes, \
    get_random_recipes, get_similar_recipes, autocomplete_recipes, get_taste_by_id, get_equipment_by_id, \
    get_ingredients_by_id, get_nutrition_by_id, get_steps_by_id, get_summary_by_id, get_cuisine_by_id

router = APIRouter(
    prefix="/recipes",
    tags=['recipes'],
    responses={404: {"description": "Not found"}}
)


@router.get("")
async def router_get_recipes():
    response = await get_recipes()
    return response


@router.post("")
async def router_post_recipes():
    response = await post_recipes()
    return response


@router.get("/{recipe_id}")
async def router_get_recipe_by_id(recipe_id: int):
    response = await get_recipe_by_id(recipe_id)
    return response


@router.get("/<str:title>")
async def router_get_recipe_by_title(title: str):
    response = await get_recipe_by_title(title)
    return response


@router.get("/top")
async def router_get_top_recipes():
    response = await get_top_recipes()
    return response


@router.get("/random")
async def router_get_random_recipes():
    response = await get_random_recipes()
    return response


@router.get("/{recipe_id}/similar")
async def router_get_similar_recipes(recipe_id: int):
    response = await get_similar_recipes(recipe_id)
    return response


@router.get("/autocomplete")
async def router_autocomplete_recipes():
    response = await autocomplete_recipes()
    return response


@router.get("/{recipe_id}/tasteWidget")
async def router_get_taste_by_id(recipe_id: int):
    response = await get_taste_by_id(recipe_id)
    return response


@router.get("/{recipe_id}/equipmentWidget")
async def router_get_equipment_by_id(recipe_id: int):
    response = await get_equipment_by_id(recipe_id)
    return response


@router.get("/{recipe_id}/ingredientWidget")
async def router_get_ingredients_by_id(recipe_id: int):
    response = await get_ingredients_by_id(recipe_id)
    return response


@router.get("/{recipe_id}/nutritionWidget")
async def router_get_nutrition_by_id(recipe_id: int):
    response = await get_nutrition_by_id(recipe_id)
    return response


@router.get("/{recipe_id}/stepsWidget")
async def router_get_steps_by_id(recipe_id: int):
    response = await get_steps_by_id(recipe_id)
    return response


@router.get("/{recipe_id}/summaryWidget")
async def router_get_summary_by_id(recipe_id: int):
    response = await get_summary_by_id(recipe_id)
    return response


@router.get("/{recipe_id}/cuisineWidget")
async def router_get_cuisine_by_id(recipe_id: int):
    response = await get_cuisine_by_id(recipe_id)
    return response
