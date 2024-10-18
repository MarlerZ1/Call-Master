from datetime import datetime

from cryptography.fernet import Fernet
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import TIMESTAMP

from config import SECRET_KEY
from databases import Base, SessionLocal


class ClientModel(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=True)
    middle_name = Column(String(30), nullable=True)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    password = Column(String(250), nullable=False)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    @staticmethod
    def create_client(client, db):
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

    @staticmethod
    def get_client_by_id(clientId, db):
        return db.query(ClientModel).filter(ClientModel.id == clientId).first()

    @staticmethod
    def change_email(client, email, db):
        client.email = email.email
        db.commit()

    @staticmethod
    def change_phone(client, phone, db):
        client.phone_number = phone.phone_number
        db.commit()

    @staticmethod
    def change_password(client, password, db):
        client.password = Fernet(SECRET_KEY).encrypt(password.password.encode()).decode()
        db.commit()


class SpecialistModel(Base):
    __tablename__ = "specialist"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=True)
    middle_name = Column(String(30), nullable=True)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    password = Column(String(250), nullable=False)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    @staticmethod
    def create_specialist_with_mtm_relation(specialist, db):
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
            return -1

        for specialization in specialist.specialization:
            db.add(SpecialistSpecializationsMTM(
                specialist_id=specialist_model.id,
                specialization_id=db.query(SpecializationsModels).filter(
                    SpecializationsModels.cypher == specialization.value).first().id
            ))

        db.commit()

    @staticmethod
    def get_specialist_by_id(clientId, db):
        return db.query(ClientModel).filter(ClientModel.id == clientId).first()

    @staticmethod
    def change_email(client, email, db):
        client.email = email.email
        db.commit()

    @staticmethod
    def change_phone(client, phone, db):
        client.phone_number = phone.phone_number
        db.commit()

    @staticmethod
    def change_password(client, password, db):
        client.password = Fernet(SECRET_KEY).encrypt(password.password.encode()).decode()
        db.commit()
    # mtm = relationship("SpecialistSpecializationsMTM", back_populates="SpecialistModel")


class SpecializationsModels(Base):
    __tablename__ = "specialization"
    id = Column(Integer, primary_key=True)
    cypher = Column(String(10), nullable=False)
    title = Column(String(30), nullable=False)

    # mtm = relationship("SpecialistSpecializationsMTM", back_populates="SpecializationsModels")

    @classmethod
    def add_basic_specialization(cls):
        db = SessionLocal()
        db.add(
            SpecializationsModels(cypher="tv", title="cardiologist")
        )
        db.add(
            SpecializationsModels(cypher="pc", title="dermatologist")
        )
        db.commit()


class SpecialistSpecializationsMTM(Base):
    __tablename__ = "many_to_many_specialist_specialication"
    id = Column(Integer, primary_key=True)
    specialist_id = Column(Integer, ForeignKey("specialist.id"))
    specialization_id = Column(Integer, ForeignKey("specialization.id"))

    # specialist = relationship("SpecialistModel", back_populates="many_to_many_specialist_specialication")
    # specialization = relationship("SpecializationsModels", back_populates="many_to_many_specialist_specialication")
