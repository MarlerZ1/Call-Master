from app.models.service import specialist_service
from app.views.specialist import NewSpecialist, ViewSpecialist


async def create_specialist(new_specialist: NewSpecialist):
    created_specialist = await specialist_service.register(new_specialist.model_dump())
    return created_specialist


async def get_specialist_by_id(specialist_id: int):
    specialist = await specialist_service.get_client(specialist_id)
    return specialist


async def update_specialist_email(specialist_id: int, email: str):
    await specialist_service.update_email(specialist_id, email)


async def update_specialist_phone(specialist_id: int, new_phone: str):
    await specialist_service.update_phone(specialist_id, new_phone)


async def update_specialist_password(specialist_id: int, old_password: str, new_password: str):
    await specialist_service.change_password(specialist_id, old_password, new_password)