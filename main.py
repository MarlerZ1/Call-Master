import os

from cryptography.fernet import Fernet
from fastapi import FastAPI

import databases
from databases import engine
from models.models import SpecializationsModels
from controllers.routers import router as v1_router

app = FastAPI()
databases.Base.metadata.create_all(bind=engine)

SpecializationsModels.add_basic_specialization()
app.include_router(v1_router)
