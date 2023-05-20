from datetime import date
from pydantic import BaseModel, Field
from .conta import Conta


class Pagamento(BaseModel):
    id: int = Field(example=123)
    realizado_em: date = Field(example=date.today())
    conta: int | Conta = Field(example=date.today())
    comprovante: str = Field(example='http://localstack:4566/example')
    observacao: str = Field(example="Observacao de exemplo")
