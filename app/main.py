import asyncio

from app.controllers.main import RestAPI


async def run_server():
    rest_api = RestAPI()
    await rest_api.run()


if __name__ == '__main__':
    asyncio.run(run_server())
