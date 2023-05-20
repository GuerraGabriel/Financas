from datetime import date
from typing import List
from pydantic import BaseModel, Field
from .forma_pagamento import FormaPagamento
from .tag import Tag


class Conta(BaseModel):
    id: int = Field(example=123)
    nome: str = Field(example="Luz")
    valor: int = Field(example=1000)
    compra_em: date = Field(example=date.today())
    metodo_pagamento: int | FormaPagamento = Field(example=123)
    parcelas: int = Field(example=5, default=0)
    tags: List[int] | Tag
    debito_automatico: bool = Field(example=True, default=False)

