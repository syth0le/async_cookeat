from fastapi import APIRouter, Depends, Response, Query
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


@router.get("/{identificator}",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_recipe(identificator: Union[int, str],
                            _response: Response,
                            db: Session = Depends(get_db)):
    response = await single.get_recipe(db=db, identificator=identificator)
    return response


@router.patch("/{identificator}",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_patch_recipe(identificator: Optional[Union[int, str]],
                              _response: Response,
                              db: Session = Depends(get_db)):
    response = await single.patch_recipe(db=db, identificator=identificator)
    return response


@router.delete("/{identificator}",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_delete_recipe(identificator: Optional[Union[int, str]],
                               _response: Response,
                               db: Session = Depends(get_db)):
    response = await single.delete_recipe(db=db, identificator=identificator)
    return response


@router.get("",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_recipes(_response: Response,
                             db: Session = Depends(get_db),
                             limit: int = 100,
                             skip: int = 0):
    response = await many.get_recipes(db=db, limit=limit, skip=skip)
    return response


@router.post("",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_post_recipes(schema: RecipesPostRequest,
                              _response: Response,
                              db: Session = Depends(get_db)):
    response = await many.post_recipes(data=schema, db=db)
    return response


@router.get("/id/{recipe_id}", deprecated=True)  # deprecated
async def router_get_recipe_by_id(recipe_id: int,
                                  _response: Response,
                                  db: Session = Depends(get_db)):
    response = await single.get_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.patch("/id/{recipe_id}", deprecated=True)  # deprecated
async def router_patch_recipe_by_id(recipe_id: int,
                                    _response: Response,
                                    db: Session = Depends(get_db)):
    response = await single.patch_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.delete("/id/{recipe_id}", deprecated=True)  # deprecated
async def router_delete_recipe_by_id(recipe_id: int,
                                     _response: Response,
                                     db: Session = Depends(get_db)):
    response = await single.delete_recipe_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/title/{title}", deprecated=True)  # deprecated
async def router_get_recipe_by_title(title: str,
                                     _response: Response,
                                     db: Session = Depends(get_db)):
    response = await single.get_recipe_by_title(db=db, title=title)
    return response


@router.patch("/title/{title}", deprecated=True)  # deprecated
async def router_patch_recipe_by_title(title: str,
                                       _response: Response,
                                       db: Session = Depends(get_db)):
    response = await single.patch_recipe_by_title(db=db, title=title)
    return response


@router.delete("/title/{title}", deprecated=True)  # deprecated
async def router_delete_recipe_by_title(title: str,
                                        _response: Response,
                                        db: Session = Depends(get_db)):
    response = await single.delete_recipe_by_title(db=db, title=title)
    return response


@router.get("/top",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_top_recipes(_response: Response,
                                 db: Session = Depends(get_db),
                                 limit: int = 100,
                                 skip: int = 0):
    response = await top_recipes.get_top_recipes(db=db, limit=limit, skip=skip)
    return response


@router.post("/top",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_post_top_recipes(schema: TopRecipesIds,
                                  _response: Response,
                                  db: Session = Depends(get_db)):
    response = await top_recipes.post_top_recipes(db=db, schema=schema)
    return response


@router.patch("/top/{recipe_id}",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_patch_top_recipe(recipe_id: int,
                                  _response: Response,
                                  db: Session = Depends(get_db)):
    response = await top_recipes.patch_top_recipe(db=db, recipe_id=recipe_id)
    return response


@router.delete("/top/{recipe_id}",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_delete_top_recipe(recipe_id: int,
                                   _response: Response,
                                   db: Session = Depends(get_db)):
    response = await top_recipes.delete_top_recipe(db=db, recipe_id=recipe_id)
    return response


@router.get("/random",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_random_recipes(_response: Response,
                                    db: Session = Depends(get_db),
                                    limit: int = 100,
                                    skip: int = 0):
    response = await many.get_random_recipes(db=db, limit=limit, skip=skip)
    return response


@router.get("/{recipe_id}/similar",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_similar_recipes(recipe_id: int,
                                     _response: Response,
                                     db: Session = Depends(get_db),
                                     limit: int = 100,
                                     skip: int = 0):
    response = await many.get_similar_recipes(recipe_id=recipe_id, db=db, limit=limit, skip=skip)
    return response


@router.get("/autocomplete",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_autocomplete_recipes(_response: Response,
                                      db: Session = Depends(get_db)):
    response = await many.autocomplete_recipes(db=db)
    return response


@router.get("/{recipe_id}/tasteWidget",
            response_model=TasteGetResponse,
            # response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_taste_by_id(recipe_id: int,
                                 _response: Response,
                                 db: Session = Depends(get_db)):
    response = await widgets.get_taste_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/equipmentWidget",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_equipment_by_id(recipe_id: int,
                                     _response: Response,
                                     db: Session = Depends(get_db)):
    response = await widgets.get_equipment_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/ingredientWidget",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_ingredients_by_id(recipe_id: int,
                                       _response: Response,
                                       db: Session = Depends(get_db)):
    response = await widgets.get_ingredients_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/nutritionWidget",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_nutrition_by_id(recipe_id: int,
                                     _response: Response,
                                     db: Session = Depends(get_db)):
    response = await widgets.get_nutrition_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/stepsWidget",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_steps_by_id(recipe_id: int,
                                 _response: Response,
                                 db: Session = Depends(get_db)):
    response = await widgets.get_steps_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/summaryWidget",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_summary_by_id(recipe_id: int,
                                   _response: Response,
                                   db: Session = Depends(get_db)):
    response = await widgets.get_summary_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/cuisineWidget",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_cuisine_by_id(recipe_id: int,
                                   _response: Response,
                                   db: Session = Depends(get_db)):
    response = await widgets.get_cuisine_by_id(db=db, recipe_id=recipe_id)
    return response


@router.get("/{recipe_id}/categoryWidget",
            response_model=Union[main, error],
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": error}},
            status_code=200)
async def router_get_category_by_id(recipe_id: int,
                                    _response: Response,
                                    db: Session = Depends(get_db)):
    response = await widgets.get_category_by_id(db=db, recipe_id=recipe_id)
    return response
