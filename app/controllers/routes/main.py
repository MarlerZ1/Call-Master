from fastapi import APIRouter

from app.controllers.settings import config
from app.controllers.routes.client import router as client_router
from app.controllers.routes.specialist import router as specialist_router

router = APIRouter(prefix=f"/api/{config.api_prefix}", tags=['API v.1'])
router.include_router(client_router)
router.include_router(specialist_router)