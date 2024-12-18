from models.domain.interfaces import ClientServiceInterface
from models.repository.base import RepositoryInterface

from app.models.service.exceptions import WrongPhoneException, WrongEmailException


class ClientService(ClientServiceInterface):
    def __init__(self, repository: RepositoryInterface):
        self._client_repository = repository

    async def _update_client(self, client_id: int, attribute_key: str, attribute_value: str):
        updating_client = await self._client_repository.get(client_id)

        setattr(updating_client, attribute_key, attribute_value)

        return await self._client_repository.update(client_id, updating_client)

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

        try:
            return await self._update_client(client_id, 'email', new_email)
        except BaseException as e:
            raise WrongEmailException(f"Неверно задана почта. Ошибка {e}")

    async def update_phone(self, client_id: int, new_phone: str) -> None:
        try:
            ...
            # todo: осущетсвить првоерку формата почты перед сменой
        except BaseException as e:
            raise e

        try:
            return await self._update_client(client_id, 'phone_number', new_phone)
        except BaseException as e:
            raise WrongPhoneException(f"Неверно задан номер телефона. Ошибка {e}")

    async def change_password(self, client_id: int, old_password: str, new_password: str) -> None:
        try:
            ...
            # todo: осуществить првоерку пароля перед сменой
            # todo: функция хэширования пароля + соль
        except BaseException as e:
            raise e

        try:
            return await self._update_client(client_id, 'password', new_password)
        except BaseException as e:
            raise e
