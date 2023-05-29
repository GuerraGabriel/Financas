from abc import ABC, abstractmethod
from typing import List
from ..entities import Receita


class ReceitaRepository(ABC):
    
    @abstractmethod
    def __init__(self):
        ...
        
    @abstractmethod
    async def get_by_id(self, id: int) -> dict:
        ...
    
    @abstractmethod
    async def get_lasts(self, size: int, page: int) -> List[dict]:
        ...
    
    @abstractmethod
    async def create_receita(self, receita: Receita):
        ...
    
    @abstractmethod
    async def delete_receita(self, receita_id: int):
        ...

    @abstractmethod
    async def patch_receita(self, new_receita: Receita):
        ...