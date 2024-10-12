from fastapi import APIRouter

from controllers.clients import router as rt_clients
from controllers.specialists import router as rt_specialists

router = APIRouter(prefix="")
router.include_router(rt_clients)
router.include_router(rt_specialists)
