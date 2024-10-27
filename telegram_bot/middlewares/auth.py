from telegram_bot.schema.user import User
from telegram_bot.api.server import Server


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

        telegram_user = update.from_user
        server: Server = data.get("server")
        user = await server.get_user_by_id(telegram_user.id)
        bot: Bot = data.get("bot")
        if user:

            await server.put_user(
                User.map_from_aiogram_user(
                    aiogram_user=telegram_user,

                )
            )

            return await handler(update, {**data, "user": user})

        new_user = await server.create_user(
            User.map_from_aiogram_user(aiogram_user=telegram_user)
        )

        if new_user:
            # Если успешно создали, передаем данные дальше
            return await handler(update, {**data, "user": new_user})

        # Если создание не удалось, сообщаем об ошибке пользователю
        await bot.send_message(
            chat_id=telegram_user.id,
            text="Извините, не удалось создать пользователя.",
            disable_notification=True
        )

        # Удаление update в случае ошибки
        logger.error(f"Failed to create user for {telegram_user.id}")
        await update.delete()  # Удаляем только после всех действий
