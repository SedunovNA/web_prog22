from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. import tables, models
from ..database import get_session
from ..wallets import WalletsService
class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        self.wallets_service = WalletsService(session)
    def create(        self,
        user_id: int,        operation_data: models.OperationCreate,
    ) -> tables.Operation:        # Создаем операцию
        operation = tables.Operation(
            **operation_data.dict(), user_id=user_id,)
        self.session.add(operation)
        self.session.commit()
        # Обновляем общую сумму кошелька        wallet_id = operation_data.wallet_id
        wallet = self.wallets_service.get_wallet(wallet_id)
        if operation_data.kind == 'income':            wallet.total_amount += operation_data.amount
        elif operation_data.kind == 'outcome':
            if wallet.total_amount < operation_data.amount:
                raise HTTPException(status_code=400, detail="Insufficient funds in the wallet")
                wallet.total_amount -= operation_data.amount
        self.session.commit()
        return operation