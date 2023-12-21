# accountr/app.py
from fastapi import FastAPI, Depends, HTTPException
from . import api, models
from .services.wallets import WalletsService
tags_metadata = [    {
        'name': 'operations',        'description': 'Создание, редактирование, удаление и просмотр операций',
    },    {
        'name': 'wallets',        'description': 'Управление кошельками',
    },]
app = FastAPI(
    title='Accountr',    description='Сервис учета личных доходов и расходов',
    version='1.0.0',    openapi_tags=tags_metadata,
)
app.include_router(api.router)
# Эндпойнты для управления кошельками@app.post('/wallets/', response_model=models.Wallet)
def create_wallet(wallet_data: models.WalletCreate, wallets_service: WalletsService = Depends()):
    return wallets_service.create_wallet(wallet_data)
@app.get('/wallets/', response_model=models.Wallet)
def get_wallets(wallets_service: WalletsService = Depends()):
    return wallets_service.get_wallets()
@app.put('/wallets/{wallet_id}/convert/', response_model=models.Wallet)
def convert_currency(wallet_id: int, new_currency: str, wallets_service: WalletsService = Depends()):
    return wallets_service.convert_currency(wallet_id, new_currency)