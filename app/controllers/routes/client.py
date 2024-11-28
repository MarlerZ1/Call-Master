from fastapi import APIRouter

from app.controllers.actions.client import client_actions
from app.controllers.schema import UpdateEmailRequest, UpdatePhoneRequest
from app.controllers.schema import UpdatePasswordRequest

from app.views.client import NewClient, ViewClient

router = APIRouter(prefix='/client', tags=['client'])


@router.post("", response_model=ViewClient)
async def register_client(
        new_client: NewClient
):
    return await client_actions.create_client(new_client)


@router.get("/{client_id}", response_model=ViewClient)
async def get_client(
        client_id: int
):
    return await client_actions.get_client_by_id(client_id)


@router.patch("/{client_id}/email")
async def update_email(client_id: int, update_request: UpdateEmailRequest):
    return await client_actions.update_client_email(client_id, update_request.email)


@router.patch("/{client_id}/phone")
async def update_phone(client_id: int, update_request: UpdatePhoneRequest):
    return await client_actions.update_client_phone(client_id, update_request.phone)


@router.patch("/{client_id}/password")
async def update_password(client_id: int, update_request: UpdatePasswordRequest):
    return await client_actions.update_client_password(client_id, update_request.old_password, update_request.new_password)
