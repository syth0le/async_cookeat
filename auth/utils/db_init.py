import os

import databases
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from auth.settings.config import config_by_name

load_dotenv(override=True)

CONFIG = config_by_name['dev']

# user = CONFIG.USER
# password = CONFIG.PASSWORD
# postgresserver = CONFIG.POSTGRESSERVER
# AUTH_DATABASE_URL = f"postgresql://{user}:{password}@localhost:5432/{postgresserver}"

database = databases.Database(CONFIG.AUTH_DATABASE_URL)

engine = create_engine(
    CONFIG.AUTH_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
