from typing import List

from domain.entities import Debt
from domain.repositories import DebtRepository
from domain.useCases.errors.DebtNotFound import DebtNotFound
from utils.result import Ok, Result


class GetAllDebts:

    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self) -> Result[List[Debt], None]:

        debts = self.debt_repository.get_all_debts()

        return Ok(debts)
