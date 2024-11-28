from app.models.domain.interfaces import SpecialistServiceInterface
from app.models.service import specialist_service
from app.views.specialist import NewSpecialist


class SpecialistActions:
    def __init__(self, specialist_service: SpecialistServiceInterface):
        self._specialist_service = specialist_service

    async def create_specialist(self, new_specialist: NewSpecialist):
        created_specialist = await self._specialist_service.register(new_specialist.model_dump())
        return created_specialist


    async def get_specialist_by_id(self, specialist_id: int):
        specialist = await self._specialist_service.get_specialist(specialist_id)
        return specialist


    async def update_specialist_email(self, specialist_id: int, email: str):
        return await self._specialist_service.update_email(specialist_id, email)


    async def update_specialist_phone(self, specialist_id: int, new_phone: str):
        return await self._specialist_service.update_phone(specialist_id, new_phone)


    async def update_specialist_password(self, specialist_id: int, old_password: str, new_password: str):
        return await self._specialist_service.change_password(specialist_id, old_password, new_password)

specialist_actions = SpecialistActions(specialist_service)