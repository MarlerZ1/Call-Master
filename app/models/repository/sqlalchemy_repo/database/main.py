from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .settings import config

DATABASE_URL = f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"


def get_async_session(database_url: str, echo=True):
    async_engine = create_async_engine(
        database_url,
        echo=echo
    )
    return sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
