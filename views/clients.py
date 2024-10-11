from cryptography.fernet import Fernet
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import SECRET_KEY
from databases import get_db
from models.models import ClientModel
from models.schemas import EmailVerification, PhoneVerification, PasswordVerification, ClientDTO, Client

router = APIRouter(prefix="/client")


@router.post("/", status_code=status.HTTP_201_CREATED)
def index(client: Client, db: Session = Depends(get_db)):
    client = ClientModel(
        first_name=client.first_name,
        last_name=client.last_name,
        middle_name=client.middle_name,
        email=client.email,
        phone_number=client.phone_number,
        password=Fernet(SECRET_KEY).encrypt(client.password.encode()).decode(),
        timestamp=client.timestamp
    )

    db.add(client)
    db.commit()

    return f"Client registered successfully"


@router.get("/{clientId}")
def get_client(clientId: int, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.id == clientId).first()

    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)

    return ClientDTO.model_validate(client, from_attributes=True)


@router.put("/{clientId}/email")
def change_email_client(clientId: int, email: EmailVerification, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.id == clientId).first()
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)
    client.email = email.email
    db.commit()

    return "Client email updated successfully"


@router.put("/{clientId}/phone")
def change_phone_client(clientId: int, phone: PhoneVerification, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.id == clientId).first()
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)
    client.phone_number = phone.phone_number
    db.commit()

    return "Client phone number updated successfully"


@router.put("/{clientId}/password")
def change_password_client(clientId: int, password: PasswordVerification, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.id == clientId).first()
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)
    client.password = FERNET.encrypt(password.password.encode()).decode()
    db.commit()

    return "Client password changed successfully"
