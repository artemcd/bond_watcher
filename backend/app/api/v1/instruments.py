from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.database import get_session
# from backend.app.services.instrument_cache import InstrumentCache
# from backend.app.schemas import BondOut

router = APIRouter()


@router.get("/{figi}")#, response_model=BondOut)
async def get_bond(
    figi: str,
    session: AsyncSession = Depends(get_session),
):
    """
    Возвращает информацию об облигации по FIGI или ISIN.
    """
    pass
    # cache = InstrumentCache(session=session)
    # bond = await cache.get_bond(figi)
    # if bond is None:
    #     raise HTTPException(status_code=404, detail="Bond not found")
    # return bond


@router.get("/")#, response_model=List[BondOut])
async def search_bonds(
    query: str,
    session: AsyncSession = Depends(get_session),
    limit: int = 20,
):
    """
    Поиск облигаций по текстовому запросу (по ISIN, FIGI, названию).
    """
    pass
    # cache = InstrumentCache(session=session)
    # return await cache.search(query=query, limit=limit)