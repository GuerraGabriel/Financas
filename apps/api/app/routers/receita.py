from typing import List
from fastapi.routing import APIRouter
from fastapi import status
from ..entities.receita import Receita
from ..composers.receita import get_use_case

router = APIRouter(prefix='/receita', tags=['Receita'])
use_case = get_use_case()

@router.get('/lasts')
async def get_last_receitas(size=10, page=0) -> List[Receita]:
    return await use_case.get_lasts(size, page)

@router.get('/{receita_id}')
async def get_receita_by_id(receita_id: int) -> Receita:
    return await use_case.get_by_id(receita_id)
    
@router.post('/new', status_code=status.HTTP_201_CREATED)
async def create_create_receita(receita: Receita) -> None:
    use_case.create_receita(receita)
    
@router.delete('/{receita_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_receita_by_id(receita_id: int) -> None:
    use_case.delete_receita(receita_id)
    
@router.patch('/{receita_id}', status_code=status.HTTP_204_NO_CONTENT)
async def patch_partial_receita_by_id(receita_id: int, new_receita: Receita) -> None:
    use_case.update_receita(receita_id, new_receita)
    
@router.put('', status_code=status.HTTP_204_NO_CONTENT)
async def put_receita_by_id(receita: Receita) -> None:
    use_case.update_or_create_receita(receita)