from typing import Union

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from api.handlers.utility import UtilitySingleRepository as utility_single, UtilityAllRepository as ulitity_all
from api.schemas.utility_widgets import UtilityIdsError
from api.utils.db_init import get_db
from api.utils.exceptions import Exception_404

router = APIRouter(
    prefix="/utility",
    tags=["utility"],
    responses={404: {"description": "Not found"}}
)


@router.get("/categories",
            response_model=main,
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": UtilityIdsError}},
            status_code=200)
async def router_get_categories(_response: Response,
                                db: Session = Depends(get_db),
                                limit: int = 100,
                                skip: int = 0):
    try:
        response = await ulitity_all.get_categories(db=db, limit=limit, skip=skip)
    except Exception_404 as ex:
        _response.status_code = 404
        return UtilityIdsError(status=404, name=ex.name)
    return response


@router.get("/nutrition",
            response_model=main,
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": UtilityIdsError}},
            status_code=200)
async def router_get_nutrition(_response: Response,
                               db: Session = Depends(get_db),
                               limit: int = 100,
                               skip: int = 0):
    try:
        response = await ulitity_all.get_nutrition(db=db, limit=limit, skip=skip)
    except Exception_404 as ex:
        _response.status_code = 404
        return UtilityIdsError(status=404, name=ex.name)
    return response


@router.get("/cuisines",
            response_model=main,
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": UtilityIdsError}},
            status_code=200)
async def router_get_cuisines(_response: Response,
                              db: Session = Depends(get_db),
                              limit: int = 100,
                              skip: int = 0):
    try:
        response = await ulitity_all.get_cuisines(db=db, limit=limit, skip=skip)
    except Exception_404 as ex:
        _response.status_code = 404
        return UtilityIdsError(status=404, name=ex.name)
    return response


@router.get("/ingredients",
            response_model=main,
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": UtilityIdsError}},
            status_code=200)
async def router_get_ingredients(_response: Response,
                                 db: Session = Depends(get_db),
                                 limit: int = 100,
                                 skip: int = 0):
    try:
        response = await ulitity_all.get_ingredients(db=db, limit=limit, skip=skip)
    except Exception_404 as ex:
        _response.status_code = 404
        return UtilityIdsError(status=404, name=ex.name)
    return response


@router.get("/categories/{identificator}",
            response_model=main,
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": UtilityIdsError}},
            status_code=200)
async def router_get_single_categories(identificator: str,
                                       _response: Response,
                                       db: Session = Depends(get_db)):
    try:
        response = await utility_single.get_single_category(db=db, name=identificator)
    except Exception_404 as ex:
        _response.status_code = 404
        return UtilityIdsError(status=404, name=ex.name)
    return response


@router.get("/nutrition/{identificator}",
            response_model=main,
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": UtilityIdsError}},
            status_code=200)
async def router_get_single_nutrition(identificator: Union[int, str],
                                      _response: Response,
                                      db: Session = Depends(get_db)):
    try:
        response = await utility_single.get_single_nutrition(db=db, identificator=identificator)
    except Exception_404 as ex:
        _response.status_code = 404
        return UtilityIdsError(status=404, name=ex.name)
    return response


@router.get("/cuisines/{identificator}",
            response_model=main,
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": UtilityIdsError}},
            status_code=200)
async def router_get_single_cuisines(identificator: str,
                                     _response: Response,
                                     db: Session = Depends(get_db)):
    try:
        response = await utility_single.get_single_cuisine(db=db, name=identificator)
    except Exception_404 as ex:
        _response.status_code = 404
        return UtilityIdsError(status=404, name=ex.name)
    return response


@router.get("/ingredients/{identificator}",
            response_model=main,
            response_model_exclude_none=True,
            responses={200: {"model": main}, 404: {"model": UtilityIdsError}},
            status_code=200)
async def router_get_single_ingredients(identificator: Union[int, str],
                                        _response: Response,
                                        db: Session = Depends(get_db)):
    try:
        response = await utility_single.get_single_ingredient(db=db, identificator=identificator)
    except Exception_404 as ex:
        _response.status_code = 404
        return UtilityIdsError(status=404, name=ex.name)
    return response

# @router.get("/ingredients/search")
# async def router_search_ingredients():
#     response = await search_ingredients()
#     return response
#
#
# @router.get("/ingredients/{id}/substitutes")
# async def router_ingredient_subtitles(id: int):
#     response = await get_ingredient_subtitles(id)
#     return response
#
#
# @router.get("/products/search")
# async def router_search_products(db: Session = Depends(get_db):
#     response = await search_products()
#     return response
#
#
# @router.get("/products/{id}")
# async def router_get_product_by_id(id: int, db: Session = Depends(get_db):
#     response = await get_product_by_id(db=db,id)
#     return response
#
#
# @router.get("/products/upc/{upc}/comparable}")
# async def router_get_comparable_products(db: Session = Depends(get_db):
#     response = await get_comparable_products(db=db,id)
#     return response
