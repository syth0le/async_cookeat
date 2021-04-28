async def get_recipes():
    return "get /recipes"


async def post_recipes():
    return "post /recipes"


async def get_recipe_by_id(recipe_id: int):
    return f"/recipes/{recipe_id}"


async def get_recipe_by_title(title: str):
    return f"/recipes/{title}"


async def get_top_recipes():
    return "/recipes/top"


async def get_random_recipes():
    return "/recipes/random"


async def get_similar_recipes(recipe_id):
    return f"/recipes/{recipe_id}/similar"


async def autocomplete_recipes():
    return "/recipes/autocomplete"


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
