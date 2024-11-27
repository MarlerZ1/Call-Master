from app.models.data_models.client import ClientModel
from app.models.data_models.specialist import SpecialistModel
from app.models.service.client import ClientService
from app.models.database.main import get_async_session
from app.models.database.settings import config
from app.models.service.specialist import SpecialistService

DATABASE_URL = f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
async_session = get_async_session(DATABASE_URL)
client_service = ClientService(ClientModel, async_session)
specialist_service = SpecialistService(SpecialistModel, async_session)
