import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from app.controllers.routes.main import router

from .settings import config


class RestAPI:
    def __init__(
            self,
            host=config.host,
            port=config.port,
            router: APIRouter = router,
            title="CallMasters API",
            description="CallMasters: FastAPI Backend Application",
            origins=None
    ):
        super().__init__()
        self._host = host
        self._port = port

        if router is None:
            router = APIRouter(tags=['Service Info Ping'])

            @router.get("/ping")
            async def pong():
                return {"ping": "pong!"}

        self._router = router

        default_origins = [
            "*"
        ]
        self._origins = default_origins if origins is None else origins
        self._app = self._create_application(title, description, self._router)

    def _create_application(self, title, description, router) -> FastAPI:
        app = FastAPI(title=title, description=description)
        app.include_router(router)
        app.add_middleware(
            CORSMiddleware,
            allow_origins=self._origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        return app

    async def run(self):
        config = uvicorn.Config(app=self._app, host=self._host, port=self._port)
        server = uvicorn.Server(config=config)
        await server.serve()
