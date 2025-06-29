from typing import Any

from tinkoff.invest import AsyncClient
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX

from backend.app.core.config import settings

class TInvestGateway:
    """Expose typed async methods masking SDK internals & retry logic."""

    def __init__(self, token: str | None = None):
        self._client = AsyncClient(token, target=INVEST_GRPC_API_SANDBOX)

    async def get_accounts(self) -> Any:
        return await self._client.users.get_accounts()

    async def get_portfolio(self, account_id: str) -> Any:
        return await self._client.operations.get_portfolio(account_id=account_id)

    async def get_bond_by_figi(self, figi: str) -> Any:
        return await self._client.instruments.get_bond_by(id_type="figi", id_=figi)