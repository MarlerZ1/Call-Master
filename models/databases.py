from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from apps.utils.main import config

# from config import DB_USER, MYSQL_DATABASE, DB_PORT, DB_HOST, MYSQL_ROOT_PASSWORD

SQLALCHEMY_DATABASE_URL = f"mysql://{config.DB_USER}:{config.MYSQL_ROOT_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.MYSQL_DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
