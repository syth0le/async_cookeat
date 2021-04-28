async def get_recipes():
    return "get /recipes"


async def post_recipes():
    return "post /recipes"


async def get_recipe_by_id(recipe_id: int):
    return f"/recipes/{recipe_id}"


async def patch_recipe_by_id(recipe_id: int):
    return f"/recipes/{recipe_id}"


async def delete_recipe_by_id(recipe_id: int):
    return f"/recipes/{recipe_id}"


async def get_recipe_by_title(title: str):
    return f"/recipes/{title}"


async def patch_recipe_by_title(title: str):
    return f"/recipes/{title}"


async def delete_recipe_by_title(title: str):
    return f"/recipes/{title}"


async def get_random_recipes():
    return "/recipes/random"


async def get_similar_recipes(recipe_id):
    return f"/recipes/{recipe_id}/similar"


async def autocomplete_recipes():
    return "/recipes/autocomplete"
