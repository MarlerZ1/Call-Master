from cryptography.fernet import Fernet
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import SECRET_KEY
from databases import get_db
from models import models
from models.models import SpecializationsModels, SpecialistModel
from models.schemas import Specialist, EmailVerification, PhoneVerification, PasswordVerification

router = APIRouter(prefix="/specialists")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_specialist(specialist: Specialist, db: Session = Depends(get_db)):
    specialist_model = SpecialistModel(
        first_name=specialist.first_name,
        last_name=specialist.last_name,
        middle_name=specialist.middle_name,
        email=specialist.email,
        phone_number=specialist.phone_number,
        password=Fernet(SECRET_KEY).encrypt(specialist.password.encode()).decode(),
        timestamp=specialist.timestamp,
    )

    try:
        db.add(specialist_model)
        db.flush()
    except:
        return JSONResponse(content={"message": "There is already a user with such an email"}, status_code=409)

    for specialization in specialist.specialization:
        db.add(models.SpecialistSpecializationsMTM(
            specialist_id=specialist_model.id,
            specialization_id=db.query(SpecializationsModels).filter(
                SpecializationsModels.cypher == specialization.value).first().id
        ))

    db.commit()

    return f"Client registered successfully"


@router.put("/{specialistId}/email")
def change_email_specialist(specialistId: int, email: EmailVerification, db: Session = Depends(get_db)):
    client = db.query(SpecialistModel).filter(SpecialistModel.id == specialistId).first()
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    client.email = email.email
    db.commit()

    return "Specialist email updated successfully"


@router.put("/{specialistId}/phone")
def change_phone_specialist(specialistId: int, phone: PhoneVerification, db: Session = Depends(get_db)):
    client = db.query(SpecialistModel).filter(SpecialistModel.id == specialistId).first()
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    client.phone_number = phone.phone_number
    db.commit()

    return "Specialist phone number updated successfully"


@router.put("/{specialistId}/password")
def change_password_specialist(specialistId: int, password: PasswordVerification, db: Session = Depends(get_db)):
    client = db.query(SpecialistModel).filter(SpecialistModel.id == specialistId).first()
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    client.password = Fernet(SECRET_KEY).encrypt(password.password.encode()).decode()
    db.commit()

    return "Specialist password changed successfully"
