from domain.entities.Debt import Debt
from domain.repositories import DebtRepository

class GetDebtById:

    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, id: str) -> Debt:
        return self.debt_repository.get_by_id(id)