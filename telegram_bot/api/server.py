from .user import UserAPI
from .currency import CurrencyAPI


class Server(
    UserAPI, CurrencyAPI
):
    pass
