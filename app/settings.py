from pydantic_settings import BaseSettings, SettingsConfigDict

from app.utils.common import get_env_path


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=get_env_path(),
        env_file_encoding='utf-8',
        extra="ignore"
    )
