import psycopg2
from psycopg2 import sql

from sqlalchemy import create_engine, inspect

from app.models.repository.sqlalchemy_repo.data_models import ClientModel
from app.models.repository.sqlalchemy_repo.data_models import SpecialistModel, Speciality, SpecialistSpecializationsMTM

from app.models.repository.sqlalchemy_repo.database.settings import config


def create_db(
        host=config.host, port=config.port,
        user=config.user, password=config.password,
        database=config.database
):
    conn = None
    try:
        # 1. Устанавливаю  соединения с БД
        conn = psycopg2.connect(
            # dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # 2. Проверка существования БД
        TARGET_DB = database
        cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [TARGET_DB])
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(TARGET_DB)))
            print(f"База '{TARGET_DB}' создана успешно")
        else:
            print(f"База '{TARGET_DB}' уже существует")

        cursor.close()

    except BaseException as e:
        print(f"Ошибка: {e}")

    finally:
        if conn:
            conn.close()


def init_db(
        host=config.host, port=config.port,
        user=config.user, password=config.password,
        database=config.database
):
    database_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(database_url)
    inspector = inspect(engine)

    if not inspector.has_table(ClientModel.__tablename__):
        ClientModel.metadata.create_all(engine)
        print(f"Таблица '{ClientModel.__tablename__}' создана")
    else:
        print(f"Таблица '{ClientModel.__tablename__}' уже существует")

    if not inspector.has_table(Speciality.__tablename__):
        Speciality.metadata.create_all(engine)
        print(f"Таблица '{Speciality.__tablename__}' создана")
    else:
        print(f"Таблица '{Speciality.__tablename__}' уже существует")

    if not inspector.has_table(SpecialistModel.__tablename__):
        SpecialistModel.metadata.create_all(engine)
        print(f"Таблица '{SpecialistModel.__tablename__}' создана")
    else:
        print(f"Таблица '{SpecialistModel.__tablename__}' уже существует")

    if not inspector.has_table(SpecialistSpecializationsMTM.__tablename__):
        SpecialistModel.metadata.create_all(engine)
        print(f"Таблица '{SpecialistModel.__tablename__}' создана")
    else:
        print(f"Таблица '{SpecialistModel.__tablename__}' уже существует")


if __name__ == "__main__":
    create_db()
    # init_db()
