from fastapi import FastAPI
from api.routers.recipes import router as recipes
from api.routers.creators import router as creators

app = FastAPI()

app.include_router(recipes)
app.include_router(creators)


@app.get("/")
async def hello_world():
    return "hello_world"

