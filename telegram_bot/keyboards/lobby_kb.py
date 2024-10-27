from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def lobby_keyboard():
    kb = [
        [
            KeyboardButton(text="/АНАЛИТИКА"),
            KeyboardButton(text="/ПРОГНОЗ"),
            KeyboardButton(text="/ОБМЕНЯТЬ"),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Что вы хотите сделать?")