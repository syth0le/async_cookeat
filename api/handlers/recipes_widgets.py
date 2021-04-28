async def get_taste_by_id(recipe_id):
    return f"/{recipe_id}/tasteWidget"


async def get_equipment_by_id(recipe_id):
    return f"/{recipe_id}/equipmentWidget"


async def get_ingredients_by_id(recipe_id):
    return f"/{recipe_id}/ingredientWidget"


async def get_nutrition_by_id(recipe_id):
    return f"/{recipe_id}/nutritionWidget"


async def get_steps_by_id(recipe_id):
    return f"/{recipe_id}/stepsWidget"


async def get_summary_by_id(recipe_id):
    return f"/{recipe_id}/summaryWidget"


async def get_cuisine_by_id(recipe_id):
    return f"/{recipe_id}/cuisineWidget"
