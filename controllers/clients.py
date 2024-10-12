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
def create_client_view(client: Client, db: Session = Depends(get_db)):

    ClientModel.create_client(client, db)

    return f"Client registered successfully"


@router.get("/{clientId}")
def get_client_view(clientId: int, db: Session = Depends(get_db)):
    client = ClientModel.get_client_by_id(clientId, db)

    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)

    return ClientDTO.model_validate(client, from_attributes=True)


@router.put("/{clientId}/email")
def change_email_client_view(clientId: int, email: EmailVerification, db: Session = Depends(get_db)):
    client = ClientModel.get_client_by_id(clientId, db)
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)

    ClientModel.change_email(client, email, db)

    return "Client email updated successfully"


@router.put("/{clientId}/phone")
def change_phone_client_view(clientId: int, phone: PhoneVerification, db: Session = Depends(get_db)):
    client = ClientModel.get_client_by_id(clientId, db)
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)

    ClientModel.change_phone(client, phone, db)

    return "Client phone number updated successfully"


@router.put("/{clientId}/password")
def change_password_client_view(clientId: int, password: PasswordVerification, db: Session = Depends(get_db)):
    client = ClientModel.get_client_by_id(clientId, db)
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)

    ClientModel.change_password(client, password, db)

    return "Client password changed successfully"
