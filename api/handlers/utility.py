from typing import Union

from sqlalchemy.orm import Session

from api.handlers.base import BaseRepository
from api.models import Ingredient, Cuisine, Nutrition, Category
from api.utils.exceptions import Exception_404, Exception_400


class UtilitySingleRepository(BaseRepository):

    async def get_single_category(db: Session, name: str):
        data = db.query(Category).filter_by(name=name).first()
        print(type(data))
        if data is None:
            raise Exception_404(name=f"Not found category with name={name}")
        return data

    async def get_single_nutrition(db: Session, identificator: Union[int, str]):
        # если в бд есть в поле name чисто Int То будет ошибка что не найдено
        if type(identificator) is int:
            data = db.query(Nutrition).filter_by(id=identificator).first()
        elif type(identificator) is str:
            data = db.query(Nutrition).filter_by(name=identificator).first()
        else:
            raise Exception_400(name=f"Not correct type of identificator={type(identificator)}")
        if data is None:
            raise Exception_404(name=f"Not found nutrition with identificator={identificator}")
        return data

    async def get_single_cuisine(db: Session, name: str):
        data = db.query(Cuisine).filter_by(name=name).first()
        if data is None:
            raise Exception_404(name=f"Not found cuisine with name={name}")
        return data

    async def get_single_ingredient(db: Session, identificator: Union[int, str]):
        if type(identificator) is int:
            data = db.query(Ingredient).filter_by(id=identificator).first()
        elif type(identificator) is str:
            data = db.query(Ingredient).filter_by(name=identificator).first()
        else:
            raise Exception_400(name=f"Not correct type of identificator={type(identificator)}")
        if data is None:
            raise Exception_404(name=f"Not found ingredient with identificator={identificator}")
        return data


class UtilityAllRepository(BaseRepository):

    async def get_categories(db: Session, limit: int = 100, skip: int = 0) -> list:
        data = db.query(Category).offset(skip).limit(limit).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_nutrition(db: Session, limit: int = 100, skip: int = 0) -> list:
        data = db.query(Nutrition).offset(skip).limit(limit).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_cuisines(db: Session, limit: int = 100, skip: int = 0) -> list:
        data = db.query(Cuisine).offset(skip).limit(limit).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_ingredients(db: Session, limit: int = 100, skip: int = 0) -> list:
        data = db.query(Ingredient).offset(skip).limit(limit).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    # async def search_ingredients(db: Session, limit: int = 100, skip: int = 0):
    #     # return db.query(Ingredient).offset(skip).limit(limit).all()
    #     if not data:
    #         raise Exception_404(name="Not found elements")
    #     return data
    #     return f"search_ingredients"
    #
    # async def get_ingredient_subtitles(db: Session, id):
    #     if not data:
    #         raise Exception_404(name="Not found elements")
    #     return data
    #     return f"get_ingredient_subtitles {id}"
    #
    # async def search_products(db: Session, ):
    #     if not data:
    #         raise Exception_404(name="Not found elements")
    #     return data
    #     return "search_products"
    #
    # async def get_product_by_id(db: Session, id):
    #     if not data:
    #         raise Exception_404(name="Not found elements")
    #     return data
    #     return f"get_product_by_id {id}"
    #
    # async def get_comparable_products(db: Session, id):
    #     if not data:
    #         raise Exception_404(name="Not found elements")
    #     return data
    #     return f"get_comparable_products {id}"
