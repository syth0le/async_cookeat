from sqlalchemy.orm import Session

from api.handlers.base import BaseRepository
from api.models.recipes import Recipe
from api.schemas.recipes_list_responses import RecipesIds
from api.schemas.top_recipes import TopRecipesIds
from api.utils.exceptions import Exception_404, Exception_409, Exception_400


class TopRecipesRepository(BaseRepository):

    async def get_top_recipes(db: Session, limit: int = 100, skip: int = 0):
        data = db.query(Recipe).filter_by(is_top_recipe=True).offset(skip).limit(limit).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def post_top_recipes(db: Session, schema):
        temp = list()
        errors = list()
        for elem in schema.top_recipes:
            recipe = db.query(Recipe).filter_by(id=elem).first()
            try:
                recipe.is_top_recipe = True
                db.add(recipe)
                db.commit()
                db.refresh(recipe)
            except:
                errors.append(elem.name)
            temp.append(elem.name)
        if errors:
            raise Exception_409(name=f"Elements: {temp} already exists.")
        return db.query(Recipe).filter(Recipe.id.in_(temp)).all()

    async def patch_top_recipe(recipe_id: int, db: Session) -> Recipe:
        recipe = db.query(Recipe).filter_by(id=recipe_id).first()
        if recipe is None:
            raise Exception_404(name=f"Not found element with id={recipe_id}")
        try:
            recipe.is_top_recipe = False if recipe.is_top_recipe else True
            db.add(recipe)
            db.commit()
            db.refresh(recipe)
        except:
            raise Exception_400(name=f"patching error\n try to call the administrator")
        return recipe

    async def delete_top_recipe(recipe_id: int, db: Session) -> Recipe:
        recipe = db.query(Recipe).filter_by(id=recipe_id).first()
        recipe.is_top_recipe = False
        db.add(recipe)
        db.commit()
        db.refresh(recipe)
        return recipe
