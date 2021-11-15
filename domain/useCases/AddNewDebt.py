from typing import Union
from uuid import uuid4

from domain.entities import Date, Debt
from domain.entities.errors import InvalidMonth, InvalidType
from domain.repositories import DebtRepository
from domain.useCases.ports import StartDate
from utils.result import Error, Ok, Result


class AddNewDebt:

    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self,
                description: str,
                part_value: float,
                total_parts: int,
                start_date_data: StartDate,
                paid_parts: int) -> Result[Debt,
                                           Union[InvalidMonth, InvalidType]]:

        date_or_err = Date.create(
            start_date_data['year'], start_date_data['month'])

        if date_or_err.is_err():
            return Error(date_or_err.err())

        start_date = date_or_err.ok()

        debt_or_err = Debt.create(str(uuid4()),
                                  description,
                                  part_value,
                                  total_parts,
                                  start_date,
                                  paid_parts)

        if debt_or_err.is_err():
            return Error(debt_or_err.err())

        new_debt = debt_or_err.ok()

        added_debt = self.debt_repository.add(new_debt.id,
                                              new_debt.description,
                                              new_debt.part_value,
                                              new_debt.total_parts,
                                              new_debt.start_date.to_dict(),
                                              new_debt.total_value,
                                              new_debt.paid_parts,
                                              new_debt.remaining_parts,
                                              new_debt.remaining_value)
        return Ok(added_debt)
