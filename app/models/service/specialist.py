from sqlalchemy import select

from app.models.domain.interfaces import SpecialistServiceInterface
from app.models.repository.base import RepositoryInterface
from app.models.repository.sqlalchemy_repo.data_models.specialist import SpecialistModel, SpecialistSpecializationsMTM, \
    Speciality


class SpecialistService(SpecialistServiceInterface):
    def __init__(self, repository: RepositoryInterface):
        self._specialist_repository = repository

    async def register(self, new_specialist: dict) -> SpecialistModel:
        # todo: осуществить проверку пароля
        # todo: осуществить проверку телефона
        # todo: осуществить проверку почты

        async with self._specialist_repository._engine() as session:
            try:
                tv = await session.execute(select(Speciality).where(Speciality.name == "tv"))
                if not tv.scalars().first():
                    session.add(Speciality(name="tv"))
                    await session.commit()
                pc = await session.execute(select(Speciality).where(Speciality.name == "pc"))
                if not pc.scalars().first():
                    session.add(Speciality(name="pc"))
                    await session.commit()

                specializations = new_specialist['specialization']
                del new_specialist['specialization']

                specialist_model = self._specialist_repository.model(
                    first_name=new_specialist["first_name"],
                    last_name=new_specialist["last_name"],
                    middle_name=new_specialist["middle_name"],
                    email=new_specialist["email"],
                    phone_number=new_specialist["phone_number"],
                    password=new_specialist["password"]
                )
                session.add(specialist_model)

                for specialization in specializations:
                    specialization_object = await session.execute(
                        select(Speciality).where(Speciality.name == specialization.value))
                    session.add(SpecialistSpecializationsMTM(
                        specialist_id=specialist_model.id,
                        specialization_id=specialization_object.scalars().first().id
                    ))

                await session.commit()

                return specialist_model

            except Exception as e:
                await session.rollback()
                raise

    async def get_specialist(self, specialist_id: int):
        return await self._specialist_repository.get(specialist_id)

    async def update_email(self, specialist_id: int, new_email: str) -> None:
        try:
            ...
            # todo: осущетсвить првоерку формата почты перед сменой
        except BaseException as e:
            raise e

        specialist_object = await self._specialist_repository.get(specialist_id)
        specialist_object.email = new_email

        return await self._specialist_repository.update(specialist_id, specialist_object)

    async def update_phone(self, specialist_id: int, new_phone: str) -> None:
        try:
            ...
            # todo: осущетсвить првоерку формата почты перед сменой
        except BaseException as e:
            raise e

        specialist_object = await self._specialist_repository.get(specialist_id)
        specialist_object.phone_number = new_phone

        return await self._specialist_repository.update(specialist_id, specialist_object)

    async def change_password(self, specialist_id: int, old_password: str, new_password: str) -> None:
        try:
            ...
            # todo: осуществить првоерку пароля перед сменой
            # todo: функция хэширования пароля + соль
        except BaseException as e:
            raise e

        specialist_object = await self._specialist_repository.get(specialist_id)
        specialist_object.password = new_password
        return await self._specialist_repository.update(specialist_id, specialist_object)
