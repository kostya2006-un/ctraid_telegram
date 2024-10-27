from loguru import logger
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command
from telegram_bot.core.server import Server
from aiogram.fsm.context import FSMContext
from telegram_bot.keyboards.analis_kb import get_analis_keyboard
from telegram_bot.routes.onboarding import OnboardingRouter
import re
router = Router()


@router.message(Command("АНАЛИТИКА"))
@logger.catch
async def syntax_handler(message: Message, server: Server, state: FSMContext):
    await message.delete()
    list_currency = await server.list_currency()
    await message.answer("Выбери монету для анализа", reply_markup=await get_analis_keyboard(list_currency))


@router.callback_query(OnboardingRouter.CHOOSE_ANALITIC_CURRENCY.route)
@logger.catch
async def curr_analitic(query: CallbackQuery, server: Server, state: FSMContext):
    data = query.data.split(":")[-1]

    pattern = r"(.+?)c_id(\d+)"
    match = re.match(pattern, data)

    currency = await server.currency(match.group(2))
    await query.message.answer(text=f"Монета: {currency.name}\n Обозначение: {currency.symbol}\n")