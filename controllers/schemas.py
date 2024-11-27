from datetime import datetime
from enum import Enum
from typing import List

from pydantic import EmailStr, constr, BaseModel, field_validator


class EmailVerification(BaseModel):
    email: EmailStr


class PhoneVerification(BaseModel):
    phone_number: constr(pattern=r'^\+?1?\d{9,15}$')


class PasswordVerification(BaseModel):
    password: constr(
        min_length=8,
        max_length=20
    )


class HumanVerification(BaseModel):
    first_name: str
    last_name: str | None = None
    middle_name: str | None = None

    @field_validator("last_name", "first_name", "middle_name")
    def OnlyLettersValidator(cls, value: str):
        if not value.isalpha():
            raise ValueError("Only letters are allowed for this field")
        return value


class Client(EmailVerification, PhoneVerification, PasswordVerification, HumanVerification):
    timestamp: datetime

    class Config:
        orm_mode = True


class ClientDTO(EmailVerification, PhoneVerification, HumanVerification):
    id: int
    timestamp: datetime
    password: str


class SpecializationEnum(str, Enum):
    cardiologist = 'tv'
    dermatologist = 'pc'


class Specialist(Client):
    specialization: List[SpecializationEnum]


class SpecialistDTO(Specialist):
    id: int
