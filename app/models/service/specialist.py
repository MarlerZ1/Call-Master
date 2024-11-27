from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncEngine

from app.models.repository.sqlalchemy_repo.data_models import ClientModel
from app.models.repository.sqlalchemy_repo.data_models.specialist import SpecialistModel, SpecialistSpecializationsMTM, Speciality


# class SpecializationService:
#     def __init__(self, database_engine: AsyncEngine):
#         self._database_engine = database_engine
#
#
#     async def register(self) -> None:
#
#         async with self._database_engine() as session:
#             try:
#                 tv = await session.execute(select(Speciality).where(Speciality.name == "tv"))
#                 if not tv.scalars().first():
#                     session.add(Speciality(name="tv"))
#                     await session.commit()
#                 pc = await session.execute(select(Speciality).where(Speciality.name == "pc"))
#                 if not pc.scalars().first():
#                     session.add(Speciality(name="pc"))
#                     await session.commit()
#             except Exception as e:
#                 await session.rollback()
#                 raise


class SpecialistService:
    def __init__(self, specialist_model: SpecialistModel, database_engine: AsyncEngine):
        self._specialist_model = specialist_model
        self._database_engine = database_engine


    async def register(self, new_specialist: dict) -> ClientModel:
        # todo: осуществить проверку пароля
        # todo: осуществить проверку телефона
        # todo: осуществить проверку почты

        async with self._database_engine() as session:
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

                print(new_specialist)
                print(self._specialist_model)
                specialist_model = self._specialist_model(
                    first_name=new_specialist["first_name"],
                    last_name=new_specialist["last_name"],
                    middle_name=new_specialist["middle_name"],
                    email=new_specialist["email"],
                    phone_number=new_specialist["phone_number"],
                    password=new_specialist["password"]
                    )
                session.add(specialist_model)
                print(specializations)
                for specialization in specializations:
                    # print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                    specialization_object = await session.execute(select(Speciality).where(Speciality.name ==specialization.value))
                    # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    session.add(SpecialistSpecializationsMTM(
                        specialist_id=specialist_model.id,
                        specialization_id=specialization_object.scalars().first().id
                    ))

                await session.commit()
                # await session.refresh(specialist_model)
                return specialist_model

            except Exception as e:
                await session.rollback()
                raise

    async def get_client(self, specialist_id: int) -> ClientModel:
        async with self._database_engine() as session:
            try:
                query = select(self._specialist_model).where(
                    self._specialist_model.id == specialist_id
                )
                result = await session.execute(query)
                client = result.scalars().first()
                return client
            except Exception as e:
                raise e

    async def update_email(self, specialist_id: int, new_email: str) -> None:
        async with self._database_engine() as session:
            try:
                # осущетсвить првоерку формата почты перед сменой
                stmt = (
                    update(self._specialist_model)
                    .where(self._specialist_model.id == specialist_id)
                    .values(email=new_email)
                )
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

    async def update_phone(self, specialist_id: int, new_phone: str) -> None:
        async with self._database_engine() as session:
            try:
                # todo: осущетсвить проверку формата для телефона перед сменой
                stmt = (
                    update(self._specialist_model)
                    .where(self._specialist_model.id == specialist_id)
                    .values(phone_number=new_phone)
                )
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

    async def change_password(self, specialist_id: int, old_password: str, new_password: str) -> None:
        async with self._database_engine() as session:
            try:
                # todo: осуществить првоерку пароля перед сменой

                stmt = (
                    update(self._specialist_model)
                    .where(self._specialist_model.id == specialist_id)
                    .values(password=new_password)
                )
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
