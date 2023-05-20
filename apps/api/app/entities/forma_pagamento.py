from pydantic import BaseModel, Field

class FormaPagamento(BaseModel):
    id: int = Field(example=123)
    nome: str = Field(example='Débito')
    tipo: str = Field(example='Débito')
    banco: str = Field(example='Inter')