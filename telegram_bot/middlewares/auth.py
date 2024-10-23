from typing import Dict
from aiogram import BaseMiddleware, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Update, Message, CallbackQuery, FSInputFile

from loguru import logger


class AuthMiddleware(BaseMiddleware):

    async def __call__(self, handler, update: Update, data: Dict):
        if type(update) not in [Message, CallbackQuery]:
            logger.error(f"Unknown event {update=}")
            return

        await update.delete()
