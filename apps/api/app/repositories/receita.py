from typing import List
from .bases import ReceitaRepository
from ..entities import Receita

class PostgresReceita(ReceitaRepository):
    
    def __init__(self):
        ...
        
    async def get_by_id(self, int) -> dict:
        ...
    
    async def get_lasts(self, size: int, page: int) -> List[dict]:
        ...
    
    async def create_receita(self, receita: Receita):
        ...
    
    async def delete_receita(self, receita_id: int):
        ...

    async def patch_receita(self, new_receita: Receita):
        ...