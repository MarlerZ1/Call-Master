import pytest


@pytest.mark.asyncio
async def test_client_service_flow(client_service, first_client_dict, event_loop):
    created_client = await client_service.register(first_client_dict)
    fetched_client = await client_service.get_client(created_client.id)
    assert created_client.id == fetched_client.id

    new_password = "hello,world"
    old_password = fetched_client.password
    assert fetched_client.password == old_password

    await client_service.change_password(created_client.id, old_password, new_password)
    fetched_client = await client_service.get_client(created_client.id)

    assert fetched_client.password == new_password
