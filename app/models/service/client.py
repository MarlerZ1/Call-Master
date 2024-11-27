from sqlalchemy import select, update

from models.domain.interfaces import ClientServiceInterface
from models.repository.base import RepositoryInterface


class ClientService(ClientServiceInterface):
    def __init__(self, repository: RepositoryInterface):
        self._client_repository = repository

    async def register(self, new_client: dict):
        # todo: осуществить проверку пароля
        # todo: осуществить проверку телефона
        # todo: осуществить проверку почты

        return await self._client_repository.create(new_client)

    async def get_client(self, client_id: int):
        return await self._client_repository.get(client_id)

    async def update_email(self, client_id: int, new_email: str) -> None:
        try:
            ...
            # todo: осущетсвить првоерку формата почты перед сменой
        except BaseException as e:
            raise e

        client_object = await self._client_repository.get(client_id)
        client_object.email = new_email
        return await self._client_repository.update(client_id, client_object)

    async def update_phone(self, client_id: int, new_phone: str) -> None:
        try:
            ...
            # todo: осущетсвить првоерку формата почты перед сменой
        except BaseException as e:
            raise e

        client_object = await self._client_repository.get(client_id)
        client_object.phone_number = new_phone
        return await self._client_repository.update(client_id, client_object)

    async def change_password(self, client_id: int, old_password: str, new_password: str) -> None:
        try:
            ...
            # todo: осуществить првоерку пароля перед сменой
            # todo: функция хэширования пароля + соль
        except BaseException as e:
            raise e

        client_object = await self._client_repository.get(client_id)
        client_object.password = new_password
        return await self._client_repository.update(client_id, client_object)
