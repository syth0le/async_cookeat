import os


class Config:
    SECRET = os.getenv("SECRET")
    USER = os.getenv("POSTGRES_USER")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRESSERVER = os.getenv("POSTGRES_DB_AUTH")
    AUTH_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@localhost:5432/{POSTGRESSERVER}"
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

SECRET = Config.SECRET
