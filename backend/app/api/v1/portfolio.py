"""Portfolio endpoints."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.database import get_session
# from backend.app.services.portfolio_service import PortfolioService
# from backend.app.schemas import PositionOut

router = APIRouter()


@router.get("/", )#response_model=List[PositionOut])
async def get_portfolio(
    session: AsyncSession = Depends(get_session),
    account_id: str | None = None,
):
    """
    Возвращает список текущих позиций по облигациям для аккаунта.
    Если `account_id` не указан — используется первый доступный аккаунт.
    """
    pass
    # service = PortfolioService(session=session)
    # try:
    #     return await service.fetch_positions(account_id=account_id)
    # except ValueError as exc:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))