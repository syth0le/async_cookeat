from sqlalchemy.orm import Session

from api.models.recipes import Recipe
from api.schemas.recipes_list_responses import RecipesIds
from api.schemas.top_recipes import TopRecipesIds


async def get_top_recipes(db: Session):
    return db.query(Recipe).filter_by(is_top_recipe=True).all()


async def post_top_recipes(db: Session, data):
    for elem in data.top_recipes:
        # print(elem)
        recipe = db.query(Recipe).filter_by(id=elem).first()
        recipe.is_top_recipe = True
        db.add(recipe)
        db.commit()
        db.refresh(recipe)
    return f"done {data}"


async def patch_top_recipes(recipe_id: int, db: Session):
    recipe = db.query(Recipe).filter_by(id=recipe_id).first()
    recipe.is_top_recipe = False if recipe.is_top_recipe else True
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


async def delete_top_recipes(recipe_id: int, db: Session):
    recipe = db.query(Recipe).filter_by(id=recipe_id).first()
    recipe.is_top_recipe = False
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe
