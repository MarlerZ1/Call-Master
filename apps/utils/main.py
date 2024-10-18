import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

def get_project_root():
    return Path(__file__).parent.parent.parent

def get_env_path():
    return os.path.join(get_project_root(), ".env")


class SettingsElement(BaseSettings):
    pass

class Settings(SettingsElement):
    DB_USER: str
    MYSQL_ROOT_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    MYSQL_DATABASE: str
    MYSQL_ROOT_HOST: str
    SECRET_KEY: str
    print(get_env_path())
    model_config = SettingsConfigDict(env_file=get_env_path(), case_sensitive=True)

config = Settings()
