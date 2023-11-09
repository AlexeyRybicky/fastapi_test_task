import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

"""environment variables for database communication"""
load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

SECRET = os.environ.get("SECRET")


class Setting(BaseSettings):
    api_books_prefix: str = "/api/books"
    api_authors_prefix: str = "/api/authors"
    api_profile_prefix: str = "/api/profile"
    db_url: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    db_echo: bool = False


settings = Setting()
