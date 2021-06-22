from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.orm import Session
from typing import Optional, Union, Any

from api.handlers.recipes import RecipeSingleRepository as single, RecipeAllRepository as many
from api.handlers.recipes_widgets import RecipeWidgetsRepository as widgets
from api.handlers.top_recipes import TopRecipesRepository as top_recipes
from api.schemas.post_recipes import RecipesPostRequest
from api.schemas.recipe_items import RecipeLongItem, RecipeShortItem
from api.schemas.recipe_widget import RecipeGetResponse, RecipeUpdateRequest
from api.schemas.recipes_list_responses import RecipesIdsError, RecipesLongListGetResponse, RecipesShortListGetResponse, \
    RecipesIds
from api.schemas.top_recipes import TopRecipesIds, TopRecipesGetResponse, TopRecipesIdsError
from api.schemas.utility_widgets import TasteGetResponse
from api.utils.db_init import get_db
from api.utils.exceptions import Exception_404, Exception_409, Exception_400

router = APIRouter(
    prefix="/recipes",
    tags=['recipes'],
    responses={404: {"description": "Not found"}}
)


@router.get("/{identificator}",
            response_model=Union[RecipeGetResponse, RecipesIdsError],
            response_model_exclude_none=True,
            responses={200: {"model": RecipeGetResponse}, 404: {"model": RecipesIdsError}},
            status_code=200)
async def router_get_recipe(identificator: Union[int, str],
                            _response: Response,
                            db: Session = Depends(get_db)):
    try:
        response = await single.get_recipe(db=db, identificator=identificator)
        # print(RecipeGetResponse(*response))
    except Exception_404 as ex:
        _response.status_code = 404
        return RecipesIdsError(status=404, name=ex.name)
    return response


@router.patch("/{identificator}",
              response_model=Union[RecipeGetResponse, RecipesIdsError],
              response_model_exclude_none=True,
              responses={200: {"model": RecipeGetResponse}, 404: {"model": RecipesIdsError}},
              status_code=200)
async def router_patch_recipe(identificator: Optional[Union[int, str]],
                              schema: RecipeUpdateRequest,
                              _response: Response,
                              db: Session = Depends(get_db)):
    try:
        response = await single.patch_recipe(db=db, schema=schema, identificator=identificator)
    except Exception_404 as ex:
        _response.status_code = 404
        return RecipesIdsError(status=404, name=ex.name)
    return response


@router.delete("/{identificator}",
               response_model=RecipesIdsError,
               response_model_exclude_none=True,
               responses={200: {"model": RecipesIdsError}, 404: {"model": RecipesIdsError}},
               status_code=200)
async def router_delete_recipe(identificator: Optional[Union[int, str]],
                               _response: Response,
                               db: Session = Depends(get_db)):
    try:
        response = await single.delete_recipe(db=db, identificator=identificator)
    except Exception_404 as ex:
        _response.status_code = 404
        return RecipesIdsError(status=404, name=ex.name)
    return response


@router.get("",
            response_model=Union[RecipesShortListGetResponse, RecipesLongListGetResponse, RecipesIdsError],
            response_model_exclude_none=True,
            responses={200: {"model": Union[RecipesShortListGetResponse, RecipesLongListGetResponse]},
                       404: {"model": RecipesIdsError}},
            status_code=200)
async def router_get_recipes(_response: Response,
                             db: Session = Depends(get_db),
                             limit: int = 100,
                             skip: int = 0):
    try:
        response = await many.get_recipes(db=db, limit=limit, skip=skip)
    except Exception_404 as ex:
        _response.status_code = 404
        return RecipesIdsError(status=404, name=ex.name)
    return RecipesShortListGetResponse(data=response)
    # return RecipesShortListGetResponse(data=response) if q == "short" else RecipesLongListGetResponse(data=response)


@router.post("",
             response_model=Union[RecipesIds, RecipesIdsError],
             response_model_exclude_none=True,
             responses={200: {"model": RecipesIds}, 404: {"model": RecipesIdsError}},
             status_code=200)
async def router_post_recipes(schema: RecipesPostRequest,
                              _response: Response,
                              db: Session = Depends(get_db)):
    try:
        response = await many.post_recipes(data=schema, db=db)
    except Exception_409 as ex:
        _response.status_code = 409
        return RecipesIdsError(status=409, name=ex.name)
    return RecipesIds(recipes_ids=response)


# @router.get("/id/{recipe_id}", deprecated=True)  # deprecated
# async def router_get_recipe_by_id(recipe_id: int,
#                                   _response: Response,
#                                   db: Session = Depends(get_db)):
#     response = await single.get_recipe_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.patch("/id/{recipe_id}", deprecated=True)  # deprecated
# async def router_patch_recipe_by_id(recipe_id: int,
#                                     _response: Response,
#                                     db: Session = Depends(get_db)):
#     response = await single.patch_recipe_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.delete("/id/{recipe_id}", deprecated=True)  # deprecated
# async def router_delete_recipe_by_id(recipe_id: int,
#                                      _response: Response,
#                                      db: Session = Depends(get_db)):
#     response = await single.delete_recipe_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.get("/title/{title}", deprecated=True)  # deprecated
# async def router_get_recipe_by_title(title: str,
#                                      _response: Response,
#                                      db: Session = Depends(get_db)):
#     response = await single.get_recipe_by_title(db=db, title=title)
#     return response
#
#
# @router.patch("/title/{title}", deprecated=True)  # deprecated
# async def router_patch_recipe_by_title(title: str,
#                                        _response: Response,
#                                        db: Session = Depends(get_db)):
#     response = await single.patch_recipe_by_title(db=db, title=title)
#     return response
#
#
# @router.delete("/title/{title}", deprecated=True)  # deprecated
# async def router_delete_recipe_by_title(title: str,
#                                         _response: Response,
#                                         db: Session = Depends(get_db)):
#     response = await single.delete_recipe_by_title(db=db, title=title)
#     return response


@router.get("/top",
            response_model=Union[TopRecipesGetResponse, TopRecipesIdsError],
            response_model_exclude_none=True,
            responses={200: {"model": TopRecipesGetResponse}, 404: {"model": TopRecipesIdsError}},
            status_code=200)
async def router_get_top_recipes(_response: Response,
                                 db: Session = Depends(get_db),
                                 limit: int = 100,
                                 skip: int = 0):
    try:
        response = await top_recipes.get_top_recipes(db=db, limit=limit, skip=skip)
    except Exception_404 as ex:
        _response.status_code = 404
        return TopRecipesIdsError(status=404, name=ex.name)
    return TopRecipesGetResponse(data=response)


@router.post("/top",
             response_model=Union[TopRecipesIds, TopRecipesIdsError],
             response_model_exclude_none=True,
             responses={200: {"model": TopRecipesIds}, 409: {"model": TopRecipesIdsError}},
             status_code=200)
async def router_post_top_recipes(schema: TopRecipesIds,
                                  _response: Response,
                                  db: Session = Depends(get_db)):
    try:
        response = await top_recipes.post_top_recipes(db=db, schema=schema)
    except Exception_409 as ex:
        _response.status_code = 409
        return TopRecipesIdsError(status=409, name=ex.name)
    return TopRecipesIds(top_recipes_ids=response)


@router.patch("/top/{recipe_id}",
              response_model=Union[RecipeGetResponse, TopRecipesIdsError],
              response_model_exclude_none=True,
              responses={200: {"model": RecipeGetResponse},
                         400: {"model": TopRecipesIdsError},
                         404: {"model": TopRecipesIdsError}},
              status_code=200)
async def router_patch_top_recipe(recipe_id: int,
                                  _response: Response,
                                  db: Session = Depends(get_db)):
    try:
        response = await top_recipes.patch_top_recipe(db=db, recipe_id=recipe_id)
    except (Exception_404, Exception_400) as ex:
        if isinstance(ex, Exception_400):
            status = 400
        else:
            status = 404
        _response.status_code = status
        return TopRecipesIdsError(status=status, name=ex.name)
    return response
# если че  переделать через шему и сделать там ввод статуса через поле is_top_recipe


@router.delete("/top/{recipe_id}",
            response_model=TopRecipesIdsError,
            response_model_exclude_none=True,
            responses={200: {"model": TopRecipesIdsError}, 404: {"model": TopRecipesIdsError}},
            status_code=200)
async def router_delete_top_recipe(recipe_id: int,
                                   _response: Response,
                                   db: Session = Depends(get_db)):
    try:
        response = await top_recipes.delete_top_recipe(db=db, recipe_id=recipe_id)
    except Exception_404 as ex:
        _response.status_code = 404
        return TopRecipesIdsError(status=404, name=ex.name)
    return response


@router.get("/random",
            response_model=Union[RecipesShortListGetResponse, RecipesLongListGetResponse, RecipesIdsError],
            response_model_exclude_none=True,
            responses={200: {"model": Union[RecipesShortListGetResponse, RecipesLongListGetResponse]},
                       404: {"model": RecipesIdsError}},
            status_code=200)
async def router_get_random_recipes(_response: Response,
                                    db: Session = Depends(get_db),
                                    limit: int = 100,
                                    skip: int = 0):
    try:
        response = await many.get_random_recipes(db=db, limit=limit, skip=skip)
    except Exception_404 as ex:
        _response.status_code = 404
        return RecipesIdsError(status=404, name=ex.name)
    return RecipesShortListGetResponse(data=response)
    # return RecipesShortListGetResponse(data=response) if q == "short" else RecipesLongListGetResponse(data=response)

# @router.get("/{recipe_id}/similar",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_similar_recipes(recipe_id: int,
#                                      _response: Response,
#                                      db: Session = Depends(get_db),
#                                      limit: int = 100,
#                                      skip: int = 0):
#     response = await many.get_similar_recipes(recipe_id=recipe_id, db=db, limit=limit, skip=skip)
#     return response
#
#
# @router.get("/autocomplete",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_autocomplete_recipes(_response: Response,
#                                       db: Session = Depends(get_db)):
#     response = await many.autocomplete_recipes(db=db)
#     return response
#
#
# @router.get("/{recipe_id}/tasteWidget",
#             response_model=TasteGetResponse,
#             # response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_taste_by_id(recipe_id: int,
#                                  _response: Response,
#                                  db: Session = Depends(get_db)):
#     response = await widgets.get_taste_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.get("/{recipe_id}/equipmentWidget",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_equipment_by_id(recipe_id: int,
#                                      _response: Response,
#                                      db: Session = Depends(get_db)):
#     response = await widgets.get_equipment_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.get("/{recipe_id}/ingredientWidget",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_ingredients_by_id(recipe_id: int,
#                                        _response: Response,
#                                        db: Session = Depends(get_db)):
#     response = await widgets.get_ingredients_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.get("/{recipe_id}/nutritionWidget",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_nutrition_by_id(recipe_id: int,
#                                      _response: Response,
#                                      db: Session = Depends(get_db)):
#     response = await widgets.get_nutrition_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.get("/{recipe_id}/stepsWidget",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_steps_by_id(recipe_id: int,
#                                  _response: Response,
#                                  db: Session = Depends(get_db)):
#     response = await widgets.get_steps_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.get("/{recipe_id}/summaryWidget",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_summary_by_id(recipe_id: int,
#                                    _response: Response,
#                                    db: Session = Depends(get_db)):
#     response = await widgets.get_summary_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.get("/{recipe_id}/cuisineWidget",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_cuisine_by_id(recipe_id: int,
#                                    _response: Response,
#                                    db: Session = Depends(get_db)):
#     response = await widgets.get_cuisine_by_id(db=db, recipe_id=recipe_id)
#     return response
#
#
# @router.get("/{recipe_id}/categoryWidget",
#             response_model=Union[main, error],
#             response_model_exclude_none=True,
#             responses={200: {"model": main}, 404: {"model": error}},
#             status_code=200)
# async def router_get_category_by_id(recipe_id: int,
#                                     _response: Response,
#                                     db: Session = Depends(get_db)):
#     response = await widgets.get_category_by_id(db=db, recipe_id=recipe_id)
#     return response
