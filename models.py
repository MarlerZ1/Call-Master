from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import relationship

from databases import Base


class ClientModel(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key = True)
    first_name = Column(String(30), nullable=False)
    last_name= Column(String(30), nullable=True)
    middle_name = Column(String(30), nullable=True)
    email= Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    password = Column(String(250), nullable=False)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)


class SpecialistModel(Base):
    __tablename__ = "specialist"
    id = Column(Integer, primary_key = True)
    first_name = Column(String(30), nullable=False)
    last_name= Column(String(30), nullable=True)
    middle_name = Column(String(30), nullable=True)
    email= Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    password = Column(String(250), nullable=False)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)


    # mtm = relationship("SpecialistSpecializationsMTM", back_populates="SpecialistModel")
class SpecializationsModels(Base):
    __tablename__ = "specialization"
    id = Column(Integer, primary_key=True)
    cypher = Column(String(10), nullable=False)
    title = Column(String(30), nullable=False)

    # mtm = relationship("SpecialistSpecializationsMTM", back_populates="SpecializationsModels")


class SpecialistSpecializationsMTM(Base):
    __tablename__ = "many_to_many_specialist_specialication"
    id = Column(Integer, primary_key=True)
    specialist_id = Column(Integer, ForeignKey("specialist.id"))
    specialization_id = Column(Integer, ForeignKey("specialization.id"))

    # specialist = relationship("SpecialistModel", back_populates="many_to_many_specialist_specialication")
    # specialization = relationship("SpecializationsModels", back_populates="many_to_many_specialist_specialication")