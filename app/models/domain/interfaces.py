from abc import ABC

from models.repository.sqlalchemy_repo.data_models.client import ClientModel

from app.models.repository.sqlalchemy_repo.data_models.specialist import SpecialistModel


class ClientServiceInterface(ABC):

    async def register(self, new_client: dict) -> ClientModel:
        raise NotImplementedError

    async def get_client(self, client_id: int) -> ClientModel:
        raise NotImplementedError

    async def update_email(self, client_id: int, new_email: str) -> None:
        raise NotImplementedError

    async def update_phone(self, client_id: int, new_phone: str) -> None:
        raise NotImplementedError

    async def change_password(self, client_id: int, old_password: str, new_password: str) -> None:
        raise NotImplementedError


class SpecialistServiceInterface(ABC):

    async def register(self, new_specialist: dict) -> SpecialistModel:
        raise NotImplementedError

    async def get_specialist(self, specialist_id: int) -> SpecialistModel:
        raise NotImplementedError

    async def update_email(self, specialist_id: int, new_email: str) -> None:
        raise NotImplementedError

    async def update_phone(self, specialist_id: int, new_phone: str) -> None:
        raise NotImplementedError

    async def change_password(self, specialist_id: int, old_password: str, new_password: str) -> None:
        raise NotImplementedError
