from ..repositories.receita import PostgresReceita
from ..use_cases.receita import ReceitaUseCase

def get_use_case() -> ReceitaUseCase:
    db_repository = PostgresReceita()
    use_case = ReceitaUseCase(db_repository)
    return use_case
