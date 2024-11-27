from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from app.controllers.actions.client import create_client, get_client_by_id, update_client_email, update_client_phone, \
    update_client_password
from app.controllers.actions.specialist import get_specialist_by_id, update_specialist_email, create_specialist
from app.controllers.schema import UpdateEmailRequest, UpdatePhoneRequest
from app.controllers.schema import UpdatePasswordRequest

from app.views.client import NewClient, ViewClient
from app.views.specialist import NewSpecialist

router = APIRouter(prefix='/specialist', tags=['client'])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_specialist_view(new_specialist: NewSpecialist):
    return await create_specialist(new_specialist)


@router.get("/{specialistId}", response_model=ViewClient)
async def get_client(specialistId: int):
    return await get_specialist_by_id(specialistId)

@router.patch("/{specialistId}/email")
async def change_email_specialist_view(specialistId: int, update_request: UpdateEmailRequest):
    return await update_specialist_email(specialistId, update_request.email)


@router.patch("/{specialistId}/phone")
async def change_phone_specialist_view(specialistId: int, update_request: UpdatePhoneRequest):
    return  await update_specialist_email(specialistId, update_request.phone)


@router.patch("/{specialistId}/password")
async def change_password_specialist_view(specialistId: int, update_request: UpdatePasswordRequest):
    return await update_client_password(specialistId, update_request.old_password, update_request.new_password)
