import pytest

from controllers.actions.client import create_client, get_client_by_id, update_client_email


@pytest.mark.asyncio
async def test_client_service_flow(first_client_dict, event_loop):
    created_client = await create_client(first_client_dict)
    assert created_client.email == first_client_dict['email']

    existing_client = await get_client_by_id(created_client.id)
    assert existing_client is not None
    assert created_client.id == existing_client.id

    new_email = 'new@email.com'
    await update_client_email(created_client.id, new_email)

    existing_client = await get_client_by_id(created_client.id)
    assert existing_client is not None
    assert existing_client.email == new_email
