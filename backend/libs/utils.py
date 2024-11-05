import os

from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

def find_env_file(folder: str) -> str:
    """
    Encontra o arquivo .env
    :param folder: str
    :return: str
    """
    if os.path.isfile(f"{folder}/.env"):
        return f"{folder}/.env"

    if folder == "/":
        raise FileNotFoundError("Environment file not found")

    return find_env_file(os.path.dirname(folder))


class Settings(BaseSettings):
    """
    Configurações do sistema
    """

    ENVIRONMENT: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(
        env_file=find_env_file(ROOT_PATH), env_file_encoding="utf-8"
    )


settings = Settings()
