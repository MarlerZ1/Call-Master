from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncEngine

from app.models.data_models.client import ClientModel


class ClientService:
    def __init__(self, client_model: ClientModel, database_engine: AsyncEngine):
        self._client_model = client_model
        self._database_engine = database_engine

    async def register(self, new_client: dict) -> ClientModel:
        # todo: осуществить проверку пароля
        # todo: осуществить проверку телефона
        # todo: осуществить проверку почты

        async with self._database_engine() as session:
            try:
                client_model = self._client_model(**new_client)
                session.add(client_model)
                await session.commit()
                await session.refresh(client_model)
                return client_model
            except Exception as e:
                await session.rollback()
                raise

    async def get_client(self, client_id: int) -> ClientModel:
        async with self._database_engine() as session:
            try:
                query = select(self._client_model).where(
                    self._client_model.id == client_id
                )
                result = await session.execute(query)
                client = result.scalars().first()
                # print("CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENTCLIENT CLIENT CLIENT CLIENT CLIENT CLIENT CLIENT CLIENT CLIENT")
                return client
            except Exception as e:
                raise e

    async def update_email(self, client_id: int, new_email: str) -> None:
        async with self._database_engine() as session:
            try:
                # осущетсвить првоерку формата почты перед сменой
                stmt = (
                    update(self._client_model)
                    .where(self._client_model.id == client_id)
                    .values(email=new_email)
                )
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

    async def update_phone(self, client_id: int, new_phone: str) -> None:
        async with self._database_engine() as session:
            try:
                # todo: осущетсвить проверку формата для телефона перед сменой
                stmt = (
                    update(self._client_model)
                    .where(self._client_model.id == client_id)
                    .values(phone_number=new_phone)
                )
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

    async def change_password(self, client_id: int, old_password: str, new_password: str) -> None:
        async with self._database_engine() as session:
            try:
                # todo: осуществить првоерку пароля перед сменой

                stmt = (
                    update(self._client_model)
                    .where(self._client_model.id == client_id)
                    .values(password=new_password)
                )
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
