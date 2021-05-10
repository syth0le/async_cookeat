from sqlalchemy.orm import Session

from api.models import EquipmentToRecipe, IngredientToRecipe, NutritionToRecipe, Steps, Summary, Cuisine, Category
from api.models.recipes import Recipe


async def get_taste_by_id(db: Session, recipe_id: int):
    return f"/{recipe_id}/tasteWidget"


async def get_equipment_by_id(db: Session, recipe_id: int):
    return db.query(EquipmentToRecipe).filter_by(recipe_id=recipe_id).all()


async def get_ingredients_by_id(db: Session, recipe_id: int):
    return db.query(IngredientToRecipe).filter_by(recipe_id=recipe_id).all()


async def get_nutrition_by_id(db: Session, recipe_id: int):
    return db.query(NutritionToRecipe).filter_by(recipe_id=recipe_id).all()


async def get_steps_by_id(db: Session, recipe_id: int):
    return db.query(Steps).filter_by(recipe_id=recipe_id).all()


async def get_summary_by_id(db: Session, recipe_id: int):
    return db.query(Summary).filter_by(recipe_id=recipe_id).all()


async def get_cuisine_by_id(db: Session, recipe_id: int):
    cuisine = db.query(Recipe.cuisine).filter_by(id=recipe_id).first()
    return db.query(Cuisine).filter_by(name=cuisine).all()


async def get_category_by_id(db: Session, recipe_id: int):
    category = db.query(Recipe.category).filter_by(id=recipe_id).first()
    return db.query(Category).filter_by(name=category).all()

## так  правильнее искать  load_only()
    # user = session.query(User).\
    #     filter(User.validation == request.cookies.get("validation")).\
    #     options(load_only("id")).\
    #     one()