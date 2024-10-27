from aiogram.fsm.context import FSMContext
from telegram_bot.api.server import Server
from loguru import logger
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import CommandObject
from telegram_bot.views.lobby import lobby_view
router = Router()


@router.message(CommandStart())
@logger.catch
async def start_handler(message: Message, server: Server, state: FSMContext, command: CommandObject):
    await state.clear()
    await message.answer(**lobby_view(),disable_notification=True)
