
# accountr/api/wallets.py
from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, services
router = APIRouter()
@router.post(
    '/',    response_model=models.Wallet,
    status_code=status.HTTP_201_CREATED,)
def create_wallet(    wallet_data: models.WalletCreate,
    wallets_service: services.WalletsService = Depends(),):
    return wallets_service.create_wallet(wallet_data)
@router.post('/convert')
def convert_currency(
    conversion_data: models.CurrencyConversion,    wallets_service: services.WalletsService = Depends(),
):    return wallets_service.convert_currency(conversion_data)