from pydantic_settings import SettingsConfigDict

from app.settings import AppSettings


class Settings(AppSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_"
    )

    host: str
    port: int
    api_prefix: str


config = Settings()
