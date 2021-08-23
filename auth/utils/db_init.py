import os

import databases
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker


load_dotenv(override=True)
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
postgresserver = os.getenv("POSTGRES_DB_AUTH")
SECRET = os.getenv("SECRET")

AUTH_DATABASE_URL = f"postgresql://{user}:{password}@localhost:5432/{postgresserver}"

database = databases.Database(AUTH_DATABASE_URL)

engine = create_engine(
    AUTH_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
