from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.handlers.utility import UtilitySingleRepository as utility_single, UtilityAllRepository as ulitity_all
from api.utils.db_init import get_db

router = APIRouter(
    prefix="/utility",
    tags=["utility"],
    responses={404: {"description": "Not found"}}
)


@router.get("/categories")
async def router_get_categories(db: Session = Depends(get_db),
                                limit: int = 100,
                                skip: int = 0):
    response = await ulitity_all.get_categories(db=db, limit=limit, skip=skip)
    return response


@router.get("/nutrition")
async def router_get_nutrition(db: Session = Depends(get_db),
                               limit: int = 100,
                               skip: int = 0):
    response = await ulitity_all.get_nutrition(db=db, limit=limit, skip=skip)
    return response


@router.get("/cuisines")
async def router_get_cuisines(db: Session = Depends(get_db),
                              limit: int = 100,
                              skip: int = 0):
    response = await ulitity_all.get_cuisines(db=db, limit=limit, skip=skip)
    return response


@router.get("/ingredients")
async def router_get_ingredients(db: Session = Depends(get_db),
                                 limit: int = 100,
                                 skip: int = 0):
    response = await ulitity_all.get_ingredients(db=db, limit=limit, skip=skip)
    return response


@router.get("/categories/{identificator}")
async def router_get_single_categories(identificator: str, db: Session = Depends(get_db)):
    response = await utility_single.get_single_category(db=db, name=identificator)
    return response


@router.get("/nutrition/{identificator}")
async def router_get_single_nutrition(identificator: Union[int, str], db: Session = Depends(get_db)):
    response = await utility_single.get_single_nutrition(db=db, identificator=identificator)
    return response


@router.get("/cuisines/{identificator}")
async def router_get_single_cuisines(identificator: str, db: Session = Depends(get_db)):
    response = await utility_single.get_single_cuisine(db=db, name=identificator)
    return response


@router.get("/ingredients/{identificator}")
async def router_get_single_ingredients(identificator: Union[int, str], db: Session = Depends(get_db)):
    response = await utility_single.get_single_ingredient(db=db, identificator=identificator)
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
