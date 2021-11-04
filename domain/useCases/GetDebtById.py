from domain.entities import Debt
from domain.repositories import DebtRepository
from domain.useCases.errors.DebtNotFound import DebtNotFound

from utils import Error, Ok, Result

class GetDebtById:

    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, id: str) -> Result[Debt, DebtNotFound]:
        debt = self.debt_repository.get_by_id(id)

        if not debt:
            return Error(DebtNotFound())

        return Ok(debt)