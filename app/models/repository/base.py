from abc import ABC


class RepositoryInterface(ABC):
    async def create(self, model):
        raise NotImplementedError

    async def get(self, model_uid: int):
        raise NotImplementedError

    async def update(self, model_data):
        raise NotImplementedError

