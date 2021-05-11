from sqlalchemy.orm import Session

from api.models.recipes import Recipe
from api.schemas.recipes_list_responses import RecipesIds
from api.schemas.top_recipes import TopRecipesIds


async def get_top_recipes(db: Session, limit: int = 100, skip: int = 0):
    return db.query(Recipe).filter_by(is_top_recipe=True).offset(skip).limit(limit).all()


async def post_top_recipes(db: Session, data):
    for elem in data.top_recipes:
        recipe = db.query(Recipe).filter_by(id=elem).first()
        recipe.is_top_recipe = True
        db.add(recipe)
        db.commit()
        db.refresh(recipe)
    return f"done {data}"


async def patch_top_recipe(recipe_id: int, db: Session) -> Recipe:
    recipe = db.query(Recipe).filter_by(id=recipe_id).first()
    recipe.is_top_recipe = False if recipe.is_top_recipe else True
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


async def delete_top_recipe(recipe_id: int, db: Session) -> Recipe:
    recipe = db.query(Recipe).filter_by(id=recipe_id).first()
    recipe.is_top_recipe = False
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe
