from pydantic import BaseModel, EmailStr, constr


class UpdateEmailRequest(BaseModel):
    email: str


class UpdatePhoneRequest(BaseModel):
    phone:  str


class UpdatePasswordRequest(BaseModel):
    old_password: str
    new_password: str
