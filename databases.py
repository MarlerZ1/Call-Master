from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import DB_USER, MYSQL_DATABASE, DB_PORT, DB_HOST, MYSQL_ROOT_PASSWORD

SQLALCHEMY_DATABASE_URL = f"mysql://{DB_USER}:{MYSQL_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}/{MYSQL_DATABASE}"

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
