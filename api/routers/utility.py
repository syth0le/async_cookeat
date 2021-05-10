from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.handlers.utility import get_categories, get_nutrition, get_cuisines, get_ingredients, search_ingredients, \
    get_ingredient_subtitles, search_products, get_product_by_id, get_comparable_products
from api.utils.db_init import get_db

router = APIRouter(
    prefix="/utility",
    tags=["utility"],
    responses={404: {"description": "Not found"}}
)


@router.get("/categories")
async def router_get_categories(db: Session = Depends(get_db)):
    response = await get_categories(db=db)
    return response


@router.get("/nutrition")
async def router_get_nutrition(db: Session = Depends(get_db)):
    response = await get_nutrition(db=db)
    return response


@router.get("/cuisines")
async def router_get_cuisines(db: Session = Depends(get_db)):
    response = await get_cuisines(db=db)
    return response


@router.get("/ingredients")
async def router_get_ingredients(db: Session = Depends(get_db)):
    response = await get_ingredients(db=db)
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
