from sqlalchemy.orm import Session

from api.handlers.base import BaseRepository
from api.models.recipes import Recipe


async def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(Recipe).filter_by(id=recipe_id).first()


async def patch_recipe_by_id(db: Session, recipe_id: int):
    recipe_to_update = db.query(Recipe).filter_by(id=recipe_id).first()

    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    return f"/recipes/{recipe_id}"


async def delete_recipe_by_id(db: Session, recipe_id: int):
    return f"/recipes/{recipe_id}"


async def get_recipe_by_title(db: Session, title: str):
    return db.query(Recipe).filter_by(name=title).first()


async def patch_recipe_by_title(db: Session, title: str):
    return f"/recipes/{title}"


async def delete_recipe_by_title(db: Session, title: str):
    return f"/recipes/{title}"


async def get_recipes(db: Session, limit: int = 100, skip: int = 0):
    return db.query(Recipe).offset(skip).limit(limit).all()


async def post_recipes(self, db: Session):
    return "post /recipes"


async def get_random_recipes(self, db: Session):
    return "/recipes/random"


async def get_similar_recipes(self, db: Session, recipe_id):
    return f"/recipes/{recipe_id}/similar"


async def autocomplete_recipes(self, db: Session):
    return "/recipes/autocomplete"


# class RecipeSingleRepository(BaseRepository):
#
#     async def get_recipe_by_id(db: Session, recipe_id: int):
#         return f"/recipes/{recipe_id}"
#
#     async def patch_recipe_by_id(self, db: Session, recipe_id: int):
#         return f"/recipes/{recipe_id}"
#
#     async def delete_recipe_by_id(self, db: Session, recipe_id: int):
#         return f"/recipes/{recipe_id}"
#
#     async def get_recipe_by_title(self, db: Session, title: str):
#         return f"/recipes/{title}"
#
#     async def patch_recipe_by_title(self, db: Session, title: str):
#         return f"/recipes/{title}"
#
#     async def delete_recipe_by_title(self, db: Session, title: str):
#         return f"/recipes/{title}"
#
#
# class RecipeAllRepository(BaseRepository):
#
#     async def get_recipes(self, db: Session, limit: int = 100, skip: int = 0):
#         return db.query(Recipe).offset(skip).limit(limit).all()
#
#     async def post_recipes(self, db: Session):
#         return "post /recipes"
#
#     async def get_random_recipes(self, db: Session):
#         return "/recipes/random"
#
#     async def get_similar_recipes(self, db: Session, recipe_id):
#         return f"/recipes/{recipe_id}/similar"
#
#     async def autocomplete_recipes(self, db: Session):
#         return "/recipes/autocomplete"
