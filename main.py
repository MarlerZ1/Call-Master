import os
from cryptography.fernet import Fernet
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import databases
import models
from databases import SessionLocal, engine
from models import ClientModel, SpecializationsModels, SpecialistModel
from schemas import Client, ClientDTO, EmailVerification, PhoneVerification, PasswordVerification, Specialist

app = FastAPI()
databases.Base.metadata.create_all(bind=engine)





SECRET_KEY = os.environ.get("SECRET_KEY")
FERNET = Fernet(SECRET_KEY)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def add_basic_specialization():
    db = SessionLocal()
    db.add(
        SpecializationsModels(cypher="tv", title="cardiologist")
    )
    db.add(
        SpecializationsModels(cypher="pc", title="dermatologist")
    )
    db.commit()

add_basic_specialization()

@app.post("/clients", status_code=status.HTTP_201_CREATED)
def index(client: Client,  db: Session = Depends(get_db)):
    client = ClientModel(
        first_name=client.first_name,
        last_name=client.last_name,
        middle_name=client.middle_name,
        email=client.email,
        phone_number=client.phone_number,
        password= FERNET.encrypt(client.password.encode()).decode(),
        timestamp=client.timestamp
    )

    db.add(client)
    db.commit()

    return f"Client registered successfully"

@app.get("/clients/{clientId}")
def get_client(clientId: int,  db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.id == clientId).first()

    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)

    return ClientDTO.model_validate(client, from_attributes=True)


@app.put("/clients/{clientId}/email")
def change_email_client(clientId: int, email: EmailVerification,  db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.id == clientId).first()
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)
    client.email = email.email
    db.commit()

    return "Client email updated successfully"


@app.put("/clients/{clientId}/phone")
def change_phone_client(clientId: int, phone: PhoneVerification,  db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.id == clientId).first()
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)
    client.phone_number = phone.phone_number
    db.commit()

    return "Client phone number updated successfully"

@app.put("/clients/{clientId}/password")
def change_password_client(clientId: int, password: PasswordVerification,  db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.id == clientId).first()
    if not client:
        return JSONResponse(content={"message": "Client not found"}, status_code=404)
    client.password = FERNET.encrypt(password.password.encode()).decode()
    db.commit()

    return "Client password changed successfully"


@app.post("/specialists", status_code=status.HTTP_201_CREATED)
def create_specialist(specialist: Specialist,  db: Session = Depends(get_db)):
    specialist_model = models.SpecialistModel(
        first_name=specialist.first_name,
        last_name=specialist.last_name,
        middle_name=specialist.middle_name,
        email=specialist.email,
        phone_number=specialist.phone_number,
        password= FERNET.encrypt(specialist.password.encode()).decode(),
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
            specialization_id=db.query(SpecializationsModels).filter(SpecializationsModels.cypher == specialization.value).first().id
        ))

    db.commit()

    return f"Client registered successfully"


@app.put("/specialists/{specialistId}/email")
def change_email_specialist(specialistId: int, email: EmailVerification,  db: Session = Depends(get_db)):
    client = db.query(SpecialistModel).filter(SpecialistModel.id == specialistId).first()
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    client.email = email.email
    db.commit()

    return "Specialist email updated successfully"


@app.put("/specialists/{specialistId}/phone")
def change_phone_specialist(specialistId: int, phone: PhoneVerification,  db: Session = Depends(get_db)):
    client = db.query(SpecialistModel).filter(SpecialistModel.id == specialistId).first()
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    client.phone_number = phone.phone_number
    db.commit()

    return "Specialist phone number updated successfully"

@app.put("/specialists/{specialistId}/password")
def change_password_specialist(specialistId: int, password: PasswordVerification,  db: Session = Depends(get_db)):
    client = db.query(SpecialistModel).filter(SpecialistModel.id == specialistId).first()
    if not client:
        return JSONResponse(content={"message": "Specialist not found"}, status_code=404)
    client.password = FERNET.encrypt(password.password.encode()).decode()
    db.commit()

    return "Specialist password changed successfully"