from pydantic import BaseModel
class WalletBase(BaseModel):
    name: str
    currency: str
    total_amount: Decimal
class WalletCreate(WalletBase):
    pass
class Wallet(WalletBase):    id: int
class CurrencyConversion(BaseModel):
    source_wallet_id: int
    target_wallet_id: int
    amount: Decimal