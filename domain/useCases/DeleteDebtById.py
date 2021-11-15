from domain.repositories import DebtRepository
from domain.useCases.ports import DebtId

from utils import Error, Ok
from domain.useCases.errors import DebtNotFound
from utils import Result


class DeleteDebtById:
    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, debt_id) -> Result[DebtId, DebtNotFound]:

        found_debt = self.debt_repository.get_by_id(debt_id)

        if not found_debt:
            return Error(DebtNotFound())

        return Ok(self.debt_repository.delete_by_id(debt_id))
