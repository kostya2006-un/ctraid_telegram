from pydantic import BaseModel


class Currency(BaseModel):
    name: str
    symbol: str
    id: int