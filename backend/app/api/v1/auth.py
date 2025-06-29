from fastapi import APIRouter, Depends, HTTPException

from backend.app.services.tinvest_gateway import TInvestGateway
router = APIRouter()

gateway = TInvestGateway()

@router.get("/accounts")
async def list_accounts():
    resp = await gateway.get_accounts()
    return resp.payload.accounts