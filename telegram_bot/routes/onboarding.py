from telegram_bot.filters.route import CallbackRouteFilter, CallbackRouteTagFilter


class OnboardingRouter:
    CHOOSE_ANALITIC_CURRENCY = CallbackRouteTagFilter(action = "analitic_currency")
