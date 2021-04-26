from fastapi import APIRouter

from api.handlers.utility import get_categories, get_nutrition, get_cuisines, get_ingredients, search_ingredients, \
    get_ingredient_subtitles, search_products, get_product_by_id, get_comparable_products

router = APIRouter(
    prefix="/utility",
    tags=["utility"],
    responses={404: {"description": "Not found"}}
)


@router.get("/categories")
async def router_get_categories():
    response = await get_categories()
    return response


@router.get("/nutrition")
async def router_get_nutrition():
    response = await get_nutrition()
    return response


@router.get("/cuisines")
async def router_get_cuisines():
    response = await get_cuisines()
    return response


@router.get("/ingredients")
async def router_get_ingredients():
    response = await get_ingredients()
    return response


@router.get("/ingredients/search")
async def router_search_ingredients():
    response = await search_ingredients()
    return response


@router.get("/ingredients/{id}/substitutes")
async def router_ingredient_subtitles(id: int):
    response = await get_ingredient_subtitles(id)
    return response


@router.get("/products/search")
async def router_search_products():
    response = await search_products()
    return response


@router.get("/products/{id}")
async def router_get_product_by_id(id: int):
    response = await get_product_by_id(id)
    return response


@router.get("/products/upc/{upc}/comparable}")
async def router_get_comparable_products():
    response = await get_comparable_products(id)
    return response
