from typing import Union

from sqlalchemy.orm import Session

from api.handlers.base import BaseRepository
from api.models import Ingredient, Cuisine, Nutrition, Category


class UtilitySingleRepository(BaseRepository):

    async def get_single_category(db: Session, name: str):
        return db.query(Category).filter_by(name=name).first()

    async def get_single_nutrition(db: Session, identificator: Union[int, str]):
        if type(identificator) is int:
            return db.query(Category).filter_by(id=identificator).first()
        elif type(identificator) is str:
            return db.query(Category).filter_by(name=identificator).first()
        else:
            return {"title": identificator, "message": "can't get"}

    async def get_single_cuisine(db: Session, name: str):
        return db.query(Cuisine).filter_by(name=name).first()

    async def get_single_ingredient(db: Session, identificator: Union[int, str]):
        if type(identificator) is int:
            return db.query(Ingredient).filter_by(id=identificator).first()
        elif type(identificator) is str:
            return db.query(Ingredient).filter_by(name=identificator).first()
        else:
            return {"title": identificator, "message": "can't get"}


class UtilityAllRepository(BaseRepository):

    async def get_categories(db: Session, limit: int = 100, skip: int = 0):
        return db.query(Category).offset(skip).limit(limit).all()

    async def get_nutrition(db: Session, limit: int = 100, skip: int = 0):
        return db.query(Nutrition).offset(skip).limit(limit).all()

    async def get_cuisines(db: Session, limit: int = 100, skip: int = 0):
        return db.query(Cuisine).offset(skip).limit(limit).all()

    async def get_ingredients(db: Session, limit: int = 100, skip: int = 0):
        return db.query(Ingredient).offset(skip).limit(limit).all()

    # async def search_ingredients(db: Session, limit: int = 100, skip: int = 0):
    #     # return db.query(Ingredient).offset(skip).limit(limit).all()
    #     return f"search_ingredients"
    #
    # async def get_ingredient_subtitles(db: Session, id):
    #     return f"get_ingredient_subtitles {id}"
    #
    # async def search_products(db: Session, ):
    #     return "search_products"
    #
    # async def get_product_by_id(db: Session, id):
    #     return f"get_product_by_id {id}"
    #
    # async def get_comparable_products(db: Session, id):
    #     return f"get_comparable_products {id}"
