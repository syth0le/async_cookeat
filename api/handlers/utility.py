async def get_categories():
    return "get_categories"


async def get_nutrition():
    return "get_nutrition"


async def get_cuisines():
    return "get_cuisines"


async def get_ingredients():
    return "get_ingredients"


async def search_ingredients():
    return "search_ingredients"


async def get_ingredient_subtitles(id):
    return f"get_ingredient_subtitles {id}"


async def search_products():
    return "search_products"


async def get_product_by_id(id):
    return f"get_product_by_id {id}"


async def get_comparable_products(id):
    return f"get_comparable_products {id}"
