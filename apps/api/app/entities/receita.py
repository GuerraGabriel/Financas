from datetime import date
from enum import Enum
from pydantic import BaseModel, Field


class Periodicidade(Enum):
    DIARIO = 'diario'
    SEMANAL = 'semanal'
    QUINZENAL = 'quinzenal'
    MENSAL = 'mensal'
    BIMESTRAL = 'bimestral'
    TRIMESTRAL = 'trimestral'
    SEMESTRAL = 'semestral'
    ANUAL = 'anual'
    

class Receita(BaseModel):
    id: int | None = Field(example=1234)
    origem: str = Field(example="Salário")
    valor: int = Field(example=1000)
    recebido_em: date = Field(example=date.today())
    peridiciocidade: Periodicidade = Field(example=Periodicidade.MENSAL)