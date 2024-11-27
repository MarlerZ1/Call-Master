from app.views.client import NewClient, ViewClient
from app.models.service import client_service


async def create_client(new_client: NewClient) -> ViewClient:
    created_client = await client_service.register(new_client.model_dump())
    # return ViewClient.model_validate(created_client)
    return created_client

async def get_client_by_id(client_id: int):
    client = await client_service.get_client(client_id)
    return client


async def update_client_email(client_id: int, email: str):
    return await client_service.update_email(client_id, email)


async def update_client_phone(client_id: int, new_phone: str):
    return await client_service.update_phone(client_id, new_phone)


async def update_client_password(client_id: int, old_password: str, new_password: str):
    return await client_service.change_password(client_id, old_password, new_password)
