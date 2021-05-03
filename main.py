import os
import sqlalchemy
import databases
from fastapi import FastAPI

from api.routers.recipes import router as recipes
from api.routers.creators import router as creators
from api.routers.utility import router as utility
# from api.routers.ml_model import router as ml_model
# from api.routers.auth import router as auth
# from api.routers.meal_plan import router as meal_plan
from api.utils.db_init import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(recipes)
app.include_router(creators)
app.include_router(utility)
# app.include_router(ml_model)
# app.include_router(auth)
# app.include_router(meal_plan)


# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
