from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from telegram_bot.routes.onboarding import OnboardingRouter


async def get_analis_keyboard(list_currency) -> InlineKeyboardMarkup:
    keyboard = []
    for currency in list_currency:

            keyboard.append([
                InlineKeyboardButton(
                    text=f"{currency.name.upper()}",
                    callback_data=OnboardingRouter.CHOOSE_ANALITIC_CURRENCY.with_tag(currency.name+"c_id"+str(currency.id)).pack(),
                )
            ])
    # keyboard.append([
    #     InlineKeyboardButton(
    #         text="НАЗАД⬅️", callback_data=OnboardingRouter.BACK.pack()
    #     )
    # ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)