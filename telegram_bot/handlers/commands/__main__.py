from typing import Union
from aiogram import Dispatcher, Router
from .start import router as start_router
from .analis import router as analis_router


def include_routers(router: Union[Dispatcher | Router]):
    router.include_routers(start_router)
    router.include_routers(analis_router)