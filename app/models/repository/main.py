from sqlalchemy import select

from models.repository.base import RepositoryInterface
from models.repository.sqlalchemy_repo.data_models.client import ClientModel


class SQLAlchemyRepo(RepositoryInterface):
    model = None

    def __init__(self, engine):
        self._engine = engine

    async def create(self, model):
        async with self._engine() as session:
            try:
                created_model = self.model(**model)
                session.add(created_model)
                await session.commit()
                await session.refresh(created_model)
                return created_model
            except Exception as e:
                await session.rollback()
                raise

    async def get(self, model_uid: int):
        async with self._engine() as session:
            try:
                query = select(self.model).where(
                    self.model.id == model_uid
                )
                result = await session.execute(query)
                client = result.scalars().first()
                return client
            except Exception as e:
                raise e

    async def update(self, model_uid: int, model_data):
        async with self._engine() as session:
            ...


class ClientRepo(SQLAlchemyRepo):
    model = ClientModel
