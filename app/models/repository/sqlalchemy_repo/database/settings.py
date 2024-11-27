from pydantic_settings import SettingsConfigDict

from app.settings import AppSettings


class Settings(AppSettings):
    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_"
    )

    host: str
    port: str
    user: str
    password: str
    database: str

    def get_url(self, async_mode=False):
        async_prefix = "+asyncpg" if async_mode else ""
        return f"postgresql{async_prefix}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


config = Settings()
