from typing import List
from fastapi.routing import APIRouter
from ..entities.conta import Conta

router = APIRouter(prefix='/conta', tags=['Conta'])


@router.get('/lasts')
def get_last_contas(size=10, page=0) -> List[Conta]:
    ...

@router.get('/{conta_id}')
def get_conta_by_id(conta_id: int) -> Conta:
    ...
    
@router.post('/new')
def create_new_conta(conta: Conta) -> None:
    ...
    
@router.delete('/{conta_id}')
def delete_conta_by_id(conta_id: int) -> None:
    ...
    
@router.patch('/{conta_id}')
def patch_partial_conta_by_id(conta_id: int, new_conta: Conta) -> None:
    ...
    
@router.put('/{conta_id}')
def patch_conta_by_id(conta_id: int, new_conta: Conta) -> None:
    ...