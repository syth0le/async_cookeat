from sqlalchemy import func
from sqlalchemy.orm import Session

from api.handlers.base import BaseRepository
from api.models.recipes import Recipe


# async def get_recipe(db: Session, identificator: str):
#     if type(identificator) is int:
#         return db.query(Recipe).filter_by(id=identificator).first()
#     elif type(identificator) is str:
#         return db.query(Recipe).filter_by(name=identificator).first()
#     else:
#         return {"title": identificator, "message": "can't get"}
#
#
# async def patch_recipe(db: Session, identificator: str):
#     return f"/recipes/{identificator}"
#
#
# async def delete_recipe(db: Session, identificator: str):
#     if type(identificator) is int:
#         db.query(Recipe).filter_by(id=identificator).delete()
#     elif type(identificator) is str:
#         db.query(Recipe).filter_by(name=identificator).delete()
#     else:
#         return {"title": identificator, "message": "can't delete"}
#     db.commit()
#     return {"title": identificator, "message": "deleted"}
#
#
# async def get_recipe_by_id(db: Session, recipe_id: int):
#     return db.query(Recipe).filter_by(id=recipe_id).first()
#
#
# async def patch_recipe_by_id(db: Session, recipe_id: int):
#     recipe_to_update = db.query(Recipe).filter_by(id=recipe_id).first()
#
#     # db.add(db_user)
#     # db.commit()
#     # db.refresh(db_user)
#     return f"/recipes/{recipe_id}"
#
#
# async def delete_recipe_by_id(db: Session, recipe_id: int):
#     db.query(Recipe).filter_by(id=recipe_id).delete()
#     db.commit()
#     return {"recipe_id": recipe_id, "message": "deleted"}
#
#
# async def get_recipe_by_title(db: Session, title: str):
#     return db.query(Recipe).filter_by(name=title).first()
#
#
# async def patch_recipe_by_title(db: Session, title: str):
#     return f"/recipes/{title}"
#
#
# async def delete_recipe_by_title(db: Session, title: str):
#     db.query(Recipe).filter_by(name=title).delete()
#     db.commit()
#     return {"title": title, "message": "deleted"}


# async def get_recipes(db: Session, limit: int = 100, skip: int = 0):
#     return db.query(Recipe).offset(skip).limit(limit).all()
#
#
# async def post_recipes(db: Session, data):
#     temp = list()
#     print(data)
#     for recipe in data.data:
#         print(recipe)
#         print()
#         db_recipe = Recipe(**recipe.dict())
#         db.add(db_recipe)
#         db.commit()
#         db.refresh(db_recipe)
#         # temp.append(recipe["recipe_id"])
#     return f"done post {temp}"
#
#
# async def get_random_recipes(db: Session, limit: int = 10, skip: int = 0):
#     return db.query(Recipe).order_by(func.random()).offset(skip).limit(limit).all()
#
#
# async def get_similar_recipes(db: Session, recipe_id: int, limit: int = 100, skip: int = 0):
#     # return await db.query(Recipe).order_by(func.random()).offset(skip).limit(limit).all()
#     return f"/recipes/{recipe_id}/similar"
#
#
# async def autocomplete_recipes(self, db: Session):
#     return "/recipes/autocomplete"


class RecipeSingleRepository(BaseRepository):

    async def get_recipe(db: Session, identificator: str):
        if type(identificator) is int:
            return db.query(Recipe).filter_by(id=identificator).first()
        elif type(identificator) is str:
            return db.query(Recipe).filter_by(name=identificator).first()
        else:
            return {"title": identificator, "message": "can't get"}

    async def patch_recipe(db: Session, identificator: str):
        return f"/recipes/{identificator}"

    async def delete_recipe(db: Session, identificator: str):
        if type(identificator) is int:
            db.query(Recipe).filter_by(id=identificator).delete()
        elif type(identificator) is str:
            db.query(Recipe).filter_by(name=identificator).delete()
        else:
            return {"title": identificator, "message": "can't delete"}
        db.commit()
        return {"title": identificator, "message": "deleted"}

    async def get_recipe_by_id(db: Session, recipe_id: int):
        return db.query(Recipe).filter_by(id=recipe_id).first()

    async def patch_recipe_by_id(db: Session, recipe_id: int):
        recipe_to_update = db.query(Recipe).filter_by(id=recipe_id).first()

        # db.add(db_user)
        # db.commit()
        # db.refresh(db_user)
        return f"/recipes/{recipe_id}"

    async def delete_recipe_by_id(db: Session, recipe_id: int):
        db.query(Recipe).filter_by(id=recipe_id).delete()
        db.commit()
        return {"recipe_id": recipe_id, "message": "deleted"}

    async def get_recipe_by_title(db: Session, title: str):
        return db.query(Recipe).filter_by(name=title).first()

    async def patch_recipe_by_title(db: Session, title: str):
        return f"/recipes/{title}"

    async def delete_recipe_by_title(db: Session, title: str):
        db.query(Recipe).filter_by(name=title).delete()
        db.commit()
        return {"title": title, "message": "deleted"}


#
class RecipeAllRepository(BaseRepository):

    async def get_recipes(db: Session, limit: int = 100, skip: int = 0):
        return db.query(Recipe).offset(skip).limit(limit).all()

    async def post_recipes(db: Session, data):
        temp = list()
        print(data)
        for recipe in data.data:
            print(recipe)
            print()
            db_recipe = Recipe(**recipe.dict())
            db.add(db_recipe)
            db.commit()
            db.refresh(db_recipe)
            # temp.append(recipe["recipe_id"])
        return f"done post {temp}"

    async def get_random_recipes(db: Session, limit: int = 10, skip: int = 0):
        return db.query(Recipe).order_by(func.random()).offset(skip).limit(limit).all()

    async def get_similar_recipes(db: Session, recipe_id: int, limit: int = 100, skip: int = 0):
        # return await db.query(Recipe).order_by(func.random()).offset(skip).limit(limit).all()
        return f"/recipes/{recipe_id}/similar"

    async def autocomplete_recipes(self, db: Session):
        return "/recipes/autocomplete"
