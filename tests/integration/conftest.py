import pytest
from testcontainers.postgres import PostgresContainer

from app.models.data_models.client import ClientModel
from app.models.database.main import get_async_session
from app.models.database.settings import config
from app.models.service import ClientService
from app.models.utils import create_db, init_db


@pytest.fixture(scope='function')
def postgres_container():
    with PostgresContainer(
            "postgres:14",
            username='postgres',
            password='postgres'
    ) as postgres:
        yield postgres


@pytest.fixture(scope='function')
def container_config(postgres_container):
    new_config = config.copy()
    new_config.host = postgres_container.get_container_host_ip()
    new_config.port = postgres_container.get_exposed_port(postgres_container.port)
    new_config.user = postgres_container.username
    new_config.password = postgres_container.password
    new_config.database = postgres_container.dbname
    return new_config


@pytest.fixture(scope='function')
def container_url(container_config):
    return container_config.get_url(async_mode=True)


@pytest.fixture(scope='function')
def database_engine(container_config):
    create_db(
        container_config.host, container_config.port,
        container_config.user, container_config.password,
        container_config.database
    )
    init_db(
        container_config.host, container_config.port,
        container_config.user, container_config.password,
        container_config.database
    )
    return get_async_session(container_config.get_url(async_mode=True))


@pytest.fixture
def first_client_dict():
    return {
        'first_name': "Иван",
        'last_name': "Иванов",
        'middle_name': "Иванович",
        'email': "ivanov@mail.ru",
        'phone_number': "+79876543210",
        'password': "qwerty"
    }


@pytest.fixture(scope='function')
def client_service(database_engine):
    return ClientService(ClientModel, database_engine)
