
# accountr/models/operations.py
from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'
class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]
    wallet_id: int
class OperationCreate(OperationBase):    pass
class Operation(OperationBase):
    id: int