from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.handlers.recipes import get_recipes, post_recipes, get_recipe_by_id, get_recipe_by_title, get_random_recipes, \
    autocomplete_recipes, get_similar_recipes, patch_recipe_by_id, delete_recipe_by_id, patch_recipe_by_title, \
    delete_recipe_by_title
from api.handlers.recipes_widgets import get_taste_by_id, get_equipment_by_id, get_ingredients_by_id, \
    get_nutrition_by_id, get_steps_by_id, get_summary_by_id, get_cuisine_by_id
from api.handlers.top_recipes import get_top_recipes, post_top_recipes, patch_top_recipes, delete_top_recipes
from api.schemas.post_recipes import RecipesPostRequest
from api.utils.db_init import get_db

router = APIRouter(
    prefix="/recipes",
    tags=['recipes'],
    responses={404: {"description": "Not found"}}
)


@router.get("")
async def router_get_recipes(db: Session = Depends(get_db)):
    response = await get_recipes(db=db)
    return response


@router.post("")
async def router_post_recipes(schema: RecipesPostRequest, db: Session = Depends(get_db)):
    response = await post_recipes(data=schema, db=db)
    return response


@router.get("/{recipe_id}")
async def router_get_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.patch("/{recipe_id}")
async def router_patch_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await patch_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.delete("/{recipe_id}")
async def router_delete_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await delete_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/title/{title}")
async def router_get_recipe_by_title(title: str, db: Session = Depends(get_db)):
    response = await get_recipe_by_title(db=db, title=title)
    return response


@router.patch("/title/{title}")
async def router_patch_recipe_by_title(title: str, db: Session = Depends(get_db)):
    response = await patch_recipe_by_title(db=db, title=title)
    return response


@router.delete("/title/{title}")
async def router_delete_recipe_by_title(title: str, db: Session = Depends(get_db)):
    response = await delete_recipe_by_title(db=db, title=title)
    return response


@router.get("/top")
async def router_get_top_recipes(db: Session = Depends(get_db)):
    response = await get_top_recipes(db=db)
    return response


@router.post("/top")
async def router_post_top_recipes(db: Session = Depends(get_db)):
    response = await post_top_recipes(db=db)
    return response


@router.patch("/top")
async def router_patch_top_recipes(db: Session = Depends(get_db)):
    response = await patch_top_recipes(db=db)
    return response


@router.delete("/top")
async def router_delete_top_recipes(db: Session = Depends(get_db)):
    response = await delete_top_recipes(db=db)
    return response


@router.get("/random")
async def router_get_random_recipes(db: Session = Depends(get_db)):
    response = await get_random_recipes(db=db)
    return response


@router.get("/{recipe_id}/similar")
async def router_get_similar_recipes(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_similar_recipes(recipe_id)
    return response


@router.get("/autocomplete")
async def router_autocomplete_recipes(db: Session = Depends(get_db)):
    response = await autocomplete_recipes(db=db)
    return response


@router.get("/{recipe_id}/tasteWidget")
async def router_get_taste_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_taste_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/equipmentWidget")
async def router_get_equipment_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_equipment_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/ingredientWidget")
async def router_get_ingredients_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_ingredients_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/nutritionWidget")
async def router_get_nutrition_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_nutrition_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/stepsWidget")
async def router_get_steps_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_steps_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/summaryWidget")
async def router_get_summary_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_summary_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/cuisineWidget")
async def router_get_cuisine_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await get_cuisine_by_id(db=db, recipe_id=recipe_id)
    return response
