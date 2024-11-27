from models.repository.base import RepositoryInterface
from models.repository.sqlalchemy_repo.data_models.client import ClientModel
from sqlalchemy import select, update
from sqlalchemy.engine import row


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
            try:
                object_dict = (lambda r: {c.name: getattr(r, c.name) for c in r.__table__.columns})(model_data)

                stmt = update(self.model).where(self.model.id == model_uid).values(**object_dict)

                await session.execute(stmt)
                await session.commit()

                query = select(self.model).where(
                    self.model.id == model_uid
                )
                result = await session.execute(query)
                client = result.scalars().first()

                await session.refresh(client)
                return model_data

            except Exception as e:
                await session.rollback()
                raise e


class ClientRepo(SQLAlchemyRepo):
    model = ClientModel
