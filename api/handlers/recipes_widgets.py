from sqlalchemy.orm import Session

from api.handlers.base import BaseRepository
from api.models import EquipmentToRecipe, IngredientToRecipe, NutritionToRecipe, Steps, Summary, Cuisine, Category
from api.models.recipes import Recipe
from api.schemas.utility_widgets import TasteGetResponse
from api.utils.exceptions import Exception_404


class RecipeWidgetsRepository(BaseRepository):

    async def get_taste_by_id(db: Session, recipe_id: int):
        data = db.query(Recipe).filter_by(id=recipe_id).first()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_equipment_by_id(db: Session, recipe_id: int):
        data = db.query(EquipmentToRecipe).filter_by(recipe_id=recipe_id).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_ingredients_by_id(db: Session, recipe_id: int):
        data = db.query(IngredientToRecipe).filter_by(recipe_id=recipe_id).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_nutrition_by_id(db: Session, recipe_id: int):
        data = db.query(NutritionToRecipe).filter_by(recipe_id=recipe_id).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_steps_by_id(db: Session, recipe_id: int):
        data = db.query(Steps).filter_by(recipe_id=recipe_id).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_summary_by_id(db: Session, recipe_id: int):
        data = db.query(Summary).filter_by(recipe_id=recipe_id).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_cuisine_by_id(db: Session, recipe_id: int):
        cuisine = db.query(Recipe.cuisine).filter_by(id=recipe_id).first()
        data = db.query(Cuisine).filter_by(name=cuisine).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    async def get_category_by_id(db: Session, recipe_id: int):
        category = db.query(Recipe.category).filter_by(id=recipe_id).first()
        data = db.query(Category).filter_by(name=category).all()
        if not data:
            raise Exception_404(name="Not found elements")
        return data

    ## так  правильнее искать  load_only()
    # user = session.query(User).\
    #     filter(User.validation == request.cookies.get("validation")).\
    #     options(load_only("id")).\
    #     one()
