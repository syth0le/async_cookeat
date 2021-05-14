from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, Union

from api.handlers.recipes import RecipeSingleRepository as single, RecipeAllRepository as many
from api.handlers.recipes_widgets import RecipeWidgetsRepository as widgets
from api.handlers.top_recipes import TopRecipesRepository as top_recipes
from api.schemas.post_recipes import RecipesPostRequest
from api.schemas.top_recipes import TopRecipesIds
from api.schemas.utility_widgets import TasteGetResponse
from api.utils.db_init import get_db

router = APIRouter(
    prefix="/recipes",
    tags=['recipes'],
    responses={404: {"description": "Not found"}}
)


@router.get("/{identificator}")
async def router_get_recipe(identificator: Union[int, str], db: Session = Depends(get_db)):
    response = await single.get_recipe(db=db, identificator=identificator)
    return response


@router.patch("/{identificator}")
async def router_patch_recipe(identificator: Optional[Union[int, str]], db: Session = Depends(get_db)):
    response = await single.patch_recipe(db=db, identificator=identificator)
    return response


@router.delete("/{identificator}")
async def router_delete_recipe(identificator: Optional[Union[int, str]], db: Session = Depends(get_db)):
    response = await single.delete_recipe(db=db, identificator=identificator)
    return response


@router.get("")
async def router_get_recipes(db: Session = Depends(get_db),
                             limit: int = 100,
                             skip: int = 0):
    response = await many.get_recipes(db=db, limit=limit, skip=skip)
    return response


@router.post("")
async def router_post_recipes(schema: RecipesPostRequest, db: Session = Depends(get_db)):
    response = await many.post_recipes(data=schema, db=db)
    return response


@router.get("/id/{recipe_id}", deprecated=True)
async def router_get_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await single.get_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.patch("/id/{recipe_id}", deprecated=True)
async def router_patch_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await single.patch_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.delete("/id/{recipe_id}", deprecated=True)
async def router_delete_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await single.delete_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/title/{title}", deprecated=True)
async def router_get_recipe_by_title(title: str, db: Session = Depends(get_db)):
    response = await single.get_recipe_by_title(db=db, title=title)
    return response


@router.patch("/title/{title}", deprecated=True)
async def router_patch_recipe_by_title(title: str, db: Session = Depends(get_db)):
    response = await single.patch_recipe_by_title(db=db, title=title)
    return response


@router.delete("/title/{title}", deprecated=True)
async def router_delete_recipe_by_title(title: str, db: Session = Depends(get_db)):
    response = await single.delete_recipe_by_title(db=db, title=title)
    return response


@router.get("/top")
async def router_get_top_recipes(db: Session = Depends(get_db),
                                 limit: int = 100,
                                 skip: int = 0):
    response = await top_recipes.get_top_recipes(db=db, limit=limit, skip=skip)
    return response


@router.post("/top")
async def router_post_top_recipes(data: TopRecipesIds, db: Session = Depends(get_db)):
    response = await top_recipes.post_top_recipes(db=db, data=data)
    return response


@router.patch("/top/{recipe_id}")
async def router_patch_top_recipe(recipe_id: int, db: Session = Depends(get_db)):
    response = await top_recipes.patch_top_recipe(db=db, recipe_id=recipe_id)
    return response


@router.delete("/top/{recipe_id}")
async def router_delete_top_recipe(recipe_id: int, db: Session = Depends(get_db)):
    response = await top_recipes.delete_top_recipe(db=db, recipe_id=recipe_id)
    return response


@router.get("/random")
async def router_get_random_recipes(db: Session = Depends(get_db),
                                    limit: int = 100,
                                    skip: int = 0):
    response = await many.get_random_recipes(db=db, limit=limit, skip=skip)
    return response


@router.get("/{recipe_id}/similar")
async def router_get_similar_recipes(recipe_id: int, db: Session = Depends(get_db),
                                     limit: int = 100,
                                     skip: int = 0):
    response = await many.get_similar_recipes(recipe_id=recipe_id, db=db, limit=limit, skip=skip)
    return response


@router.get("/autocomplete")
async def router_autocomplete_recipes(db: Session = Depends(get_db)):
    response = await many.autocomplete_recipes(db=db)
    return response


@router.get("/{recipe_id}/tasteWidget", response_model=TasteGetResponse)
# @router.get("/{recipe_id}/tasteWidget")
async def router_get_taste_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await widgets.get_taste_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/equipmentWidget")
async def router_get_equipment_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await widgets.get_equipment_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/ingredientWidget")
async def router_get_ingredients_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await widgets.get_ingredients_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/nutritionWidget")
async def router_get_nutrition_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await widgets.get_nutrition_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/stepsWidget")
async def router_get_steps_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await widgets.get_steps_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/summaryWidget")
async def router_get_summary_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await widgets.get_summary_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/cuisineWidget")
async def router_get_cuisine_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await widgets.get_cuisine_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/categoryWidget")
async def router_get_category_by_id(recipe_id: int, db: Session = Depends(get_db)):
    response = await widgets.get_category_by_id(db=db, recipe_id=recipe_id)
    return response
