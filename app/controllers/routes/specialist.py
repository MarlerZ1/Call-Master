from fastapi import APIRouter
from starlette import status

from app.controllers.actions.specialist import specialist_actions
from app.controllers.schema import UpdateEmailRequest, UpdatePhoneRequest
from app.controllers.schema import UpdatePasswordRequest
from app.views.client import ViewClient
from app.views.specialist import NewSpecialist

router = APIRouter(prefix='/specialist', tags=['client'])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_specialist_view(new_specialist: NewSpecialist):
    return await specialist_actions.create_specialist(new_specialist)


@router.get("/{specialistId}", response_model=ViewClient)
async def get_client(specialistId: int):
    return await specialist_actions.get_specialist_by_id(specialistId)

@router.patch("/{specialistId}/email")
async def change_email_specialist_view(specialistId: int, update_request: UpdateEmailRequest):
    return await specialist_actions.update_specialist_email(specialistId, update_request.email)


@router.patch("/{specialistId}/phone")
async def change_phone_specialist_view(specialistId: int, update_request: UpdatePhoneRequest):
    return await specialist_actions.update_specialist_phone(specialistId, update_request.phone)



@router.patch("/{specialistId}/password")
async def change_password_specialist_view(specialistId: int, update_request: UpdatePasswordRequest):
    return await specialist_actions.update_specialist_password(specialistId, update_request.old_password, update_request.new_password)
