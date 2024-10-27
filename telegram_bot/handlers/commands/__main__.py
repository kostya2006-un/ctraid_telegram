from typing import Union
from aiogram import Dispatcher, Router
from .start import router as start_router


def include_routers(router: Union[Dispatcher | Router]):
    router.include_routers(start_router)