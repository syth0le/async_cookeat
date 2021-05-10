from sqlalchemy.orm import Session

from api.models import Ingredient, Cuisine, Nutrition, Category


async def get_categories(db: Session, limit: int = 100, skip: int = 0):
    return db.query(Category).offset(skip).limit(limit).all()


async def get_nutrition(db: Session, limit: int = 100, skip: int = 0):
    return db.query(Nutrition).offset(skip).limit(limit).all()


async def get_cuisines(db: Session, limit: int = 100, skip: int = 0):
    return db.query(Cuisine).offset(skip).limit(limit).all()


async def get_ingredients(db: Session, limit: int = 100, skip: int = 0):
    return db.query(Ingredient).offset(skip).limit(limit).all()


async def search_ingredients(db: Session, limit: int = 100, skip: int = 0):
    # return db.query(Ingredient).offset(skip).limit(limit).all()
    return f"search_ingredients"


async def get_ingredient_subtitles(db: Session, id):
    return f"get_ingredient_subtitles {id}"


async def search_products(db: Session, ):
    return "search_products"


async def get_product_by_id(db: Session, id):
    return f"get_product_by_id {id}"


async def get_comparable_products(db: Session, id):
    return f"get_comparable_products {id}"
