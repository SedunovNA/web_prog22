
# accountr/api/operations.py
from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, services
router = APIRouter()
@router.post(    '/',
    response_model=models.Operation,
    status_code=status.HTTP_201_CREATED,
)
def create_operation(
    operation_data: models.OperationCreate,
    operations_service: services.OperationsService = Depends(),
):
    return operations_service.create(operation_data)