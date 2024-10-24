from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from models.databases import get_db
from models.models import SpecialistModel
from controllers.schemas import Specialist, EmailVerification, PhoneVerification, PasswordVerification

router = APIRouter(prefix="/specialists")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_specialist_view(specialist: Specialist, db: Session = Depends(get_db)):
    try:
        SpecialistModel.create_specialist_with_mtm_relation(specialist, db)
        return f"Client registered successfully"
    except:
        return JSONResponse(content={"message": "There is already a user with such an email"}, status_code=409)


@router.put("/{specialistId}/email")
def change_email_specialist_view(specialistId: int, email: EmailVerification, db: Session = Depends(get_db)):
    client = SpecialistModel.get_specialist_by_id(specialistId, db)
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    SpecialistModel.change_email(client, email, db)

    return "Specialist email updated successfully"


@router.put("/{specialistId}/phone")
def change_phone_specialist_view(specialistId: int, phone: PhoneVerification, db: Session = Depends(get_db)):
    client = SpecialistModel.get_specialist_by_id(specialistId, db)
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    SpecialistModel.change_phone(client, phone, db)

    return "Specialist phone number updated successfully"


@router.put("/{specialistId}/password")
def change_password_specialist_view(specialistId: int, password: PasswordVerification, db: Session = Depends(get_db)):
    client = SpecialistModel.get_specialist_by_id(specialistId, db)
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    SpecialistModel.change_password(client, password, db)

    return "Specialist password changed successfully"
