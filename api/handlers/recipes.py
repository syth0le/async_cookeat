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
from api.schemas.recipe_widget import RecipeUpdateRequest
from api.utils.exceptions import Exception_400, Exception_404, Exception_409


class RecipeSingleRepository(BaseRepository):

    async def get_recipe(db: Session, identificator: str):
        if type(identificator) is int:
            data = db.query(Recipe).filter_by(id=identificator).first()
        elif type(identificator) is str:
            data = db.query(Recipe).filter_by(name=identificator).first()
        else:
            raise Exception_400(name=f"Not correct type of identificator={type(identificator)}")
        if data is None:
            raise Exception_404(name=f"Not found recipe with identificator={identificator}")
        return data

    async def patch_recipe(db: Session, schema: RecipeUpdateRequest, identificator: str):
        update_data = schema.dict(exclude_unset=True)
        db.query(Recipe).filter(Recipe.id == identificator). \
            update(update_data, synchronize_session="fetch")
        db.commit()
        updated_recipe = db.query(Recipe).filter_by(id=identificator).first()
        if updated_recipe is None:
            raise Exception_404(name=f"Not found recipe with identificator={identificator}")
        return updated_recipe

    async def delete_recipe(db: Session, identificator: str):

        if type(identificator) is int:
            recipe = db.query(Recipe).filter_by(id=identificator).first()
        elif type(identificator) is str:
            recipe = db.query(Recipe).filter_by(name=identificator).first()
        else:
            raise Exception_400(name=f"Not correct type of identificator={type(identificator)}")
        if recipe is None:
            raise Exception_404(name=f"Not found recipe with identificator={identificator}")
        db.delete(recipe)
        db.commit()
        return {"id": identificator, "status": 200, "name": f"Deleted recipe with identificator={identificator}"}

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


class RecipeAllRepository(BaseRepository):

    async def get_recipes(db: Session, limit: int = 100, skip: int = 0):
        data = db.query(Recipe).offset(skip).limit(limit).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def post_recipes(db: Session, schema):
        temp = list()
        errors = list()
        for elem in schema.data:
            recipe = Recipe(**elem.dict())
            try:
                db.add(recipe)
                db.commit()
                db.refresh(recipe)
            except:
                errors.append(elem.name)
            temp.append(elem.name)
        if errors:
            raise Exception_409(name=f"Elements: {temp} already exists.")
        return db.query(Recipe).filter(Recipe.name.in_(temp)).all()

    async def get_random_recipes(db: Session, limit: int = 10, skip: int = 0):
        data = db.query(Recipe).order_by(func.random()).offset(skip).limit(limit).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    # async def get_similar_recipes(db: Session, recipe_id: int, limit: int = 100, skip: int = 0):
    #     # return await db.query(Recipe).order_by(func.random()).offset(skip).limit(limit).all()
    #     return f"/recipes/{recipe_id}/similar"
    #
    # async def autocomplete_recipes(self, db: Session):
    #     return "/recipes/autocomplete"
