from typing import Union
from domain.entities import Debt
from domain.repositories import DebtRepository
from domain.useCases.errors import AlreadyPaidDebt, DebtNotFound
from utils import Result, Error, Ok

class PayDebtPart:

    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, id) -> Result[Debt, Union[AlreadyPaidDebt, DebtNotFound]]:
        debt = self.debt_repository.get_by_id(id)

        if not debt:
            return Error(DebtNotFound())

        if debt.is_paid():
            return Error(AlreadyPaidDebt())

        debt.paid_parts +=1
        debt.remaining_parts -=1

        debt.remaining_value = debt.remaining_parts * debt.part_value       

        paid_debt = self.debt_repository.pay_debt_part(id, debt.paid_parts, debt.remaining_parts, debt.remaining_value)

        return Ok(paid_debt)