from pydantic import BaseModel, Field

class Tag(BaseModel):
    id: int | None = Field(example=123, default=None)
    nome: str = Field(example="Tag_A")
