import os

from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(env_file=f"{ROOT_PATH}/.env", env_file_encoding="utf-8")

settings = Settings()
