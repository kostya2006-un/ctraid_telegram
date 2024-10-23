from httpx import AsyncClient


class BaseServer:

    def __init__(self, server_host: str, server_token: str):
        self.client = AsyncClient(
            base_url=f"{server_host}/api",
            headers={"Authorization": f"Token {server_token}"},
        )
