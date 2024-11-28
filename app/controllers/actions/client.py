from app.models.domain.interfaces import ClientServiceInterface
from app.models.service import client_service
from app.views.client import NewClient, ViewClient


class ClientActions:
    def __init__(self, client_service: ClientServiceInterface):
        self._client_service = client_service

    async def create_client(self, new_client: NewClient) -> ViewClient:
        created_client = await self._client_service.register(new_client.model_dump())
        return ViewClient.model_validate(created_client)

    async def get_client_by_id(self, client_id: int):
        client = await self._client_service.get_client(client_id)
        return client

    async def update_client_email(self, client_id: int, email: str):
        await self._client_service.update_email(client_id, email)

    async def update_client_phone(self, client_id: int, new_phone: str):
        await self._client_service.update_phone(client_id, new_phone)

    async def update_client_password(self, client_id: int, old_password: str, new_password: str):
        await self._client_service.change_password(client_id, old_password, new_password)

client_actions = ClientActions(client_service)