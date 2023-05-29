from typing import List
from ..entities.receita import Receita
from ..repositories import ReceitaRepository
import logging

class ReceitaUseCase:
    
    def __init__(self, db_repository: ReceitaRepository):
        self._db_repository = db_repository
    
    async def get_by_id(self, id: int) -> Receita | None:
        data = await self._db_repository.get_by_id(id)
        if data:
            return Receita(**data)

    async def get_lasts(self, size: int, page: int) -> List[Receita | None]:
        data = await self._db_repository.get_lasts(size, page)
        receitas = [Receita(**receita) for receita in data]
        return receitas

    async def create_receita(self, receita: Receita):
        if receita.id:
            logging.warning('Ignored received id to Receita')
            receita.id = None
        self._db_repository.create_receita(receita)
        
    async def delete_receita(self, receita_id: int):
        self._db_repository.delete_receita(receita_id)
        
    async def update_receita(self, old_receita: int | Receita, new_receita: Receita):

        if isinstance(old_receita, int): 
            old_receita = await self.get_by_id(old_receita)
            if not old_receita:
                raise NotImplementedError("Receita não existe")
            
        new_receita.id = old_receita.id

        if not new_receita.origem:
            new_receita.origem = old_receita.origem
            
        if not new_receita.valor:
            new_receita = old_receita.valor
            
        if not new_receita.recebido_em:
            new_receita.recebido_em = old_receita.recebido_em
            
        if not new_receita.peridiciocidade:
            new_receita.peridiciocidade = old_receita.peridiciocidade
        
        self._db_repository.patch_receita(new_receita)
    
    async def update_or_create_receita(self, receita: Receita):
        old_receita = await self.get_by_id(receita.id)
        if old_receita:
            self.update_receita(receita, receita)
        else:
            self.create_receita(receita)