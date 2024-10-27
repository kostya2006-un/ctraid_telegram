from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Annotated, Optional, List, Union

from aiogram.types import User as AiogramUser


class User(BaseModel):
    user_id: str
    is_bot: Annotated[bool, Field(default=False)]
    first_name: str
    last_name: Annotated[Optional[str], Field(default=None)]
    username: Annotated[Optional[str], Field(default=None)]

    @classmethod
    def map_from_aiogram_user(
        cls,
        aiogram_user: AiogramUser,
    ) -> User:
        return User(
            user_id=str(aiogram_user.id),
            is_bot=aiogram_user.is_bot,
            first_name=aiogram_user.first_name,
            last_name=aiogram_user.last_name,
            username=aiogram_user.username,
        )


class UserList(BaseModel):
    user_id: List[str]