from domain.entities.Debt import Debt
from domain.repositories import DebtRepository
from domain.useCases.errors.DebtNotFound import DebtNotFound
from utils.result import Error, Ok, Result

class UpdateDebtDescription:
    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, id, description = None) -> Result[Debt, DebtNotFound]:

        found_debt = self.debt_repository.get_by_id(id)

        if not found_debt:
            return Error(DebtNotFound())

        updated_debt = self.debt_repository.update_description(id, description)

        return Ok(updated_debt)
