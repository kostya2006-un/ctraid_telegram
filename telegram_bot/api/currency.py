from .base import BaseServer
from typing import List
from loguru import logger
from telegram_bot.schema.currency import Currency
from pydantic import TypeAdapter
from .exceptions import ServerAPIError


class CurrencyAPI(BaseServer):
    @logger.catch
    async def list_currency(self) -> List[Currency]:
        response = await self.client.get(f"/back/currency-list/")
        if response.status_code != 200:
            raise ServerAPIError(f"Error getting list of questions {response.read()}")
        return TypeAdapter(List[Currency]).validate_python(response.json())

    @logger.catch
    async def currency(self, curr_id) -> Currency:
        response = await self.client.get(f"/back/currency-list/{curr_id}/")
        if response.status_code != 200:
            raise ServerAPIError(f"Error getting currency {response.read()}")

        # Валидируем отдельный объект Currency
        return TypeAdapter(Currency).validate_python(response.json())

