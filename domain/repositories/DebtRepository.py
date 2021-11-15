import abc
from typing import List
from domain.useCases.ports import StartDate
from domain.entities import Debt


class DebtRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def add(self,
            _id: str,
            description: str,
            part_value: float,
            total_parts: int,
            start_date: StartDate,
            total_value: float,
            paid_parts: int,
            remaining_parts: int,
            remaining_value: float) -> Debt:
        pass

    @abc.abstractmethod
    def get_by_id(self, _id: str) -> Debt:
        pass

    @abc.abstractmethod
    def update_description(self, _id: str, description: str) -> Debt:
        pass

    @abc.abstractmethod
    def pay_debt_part(self, _id: str,
                      paid_parts: int,
                      remaining_parts: int,
                      remaining_value: float) -> Debt:
        pass

    @abc.abstractmethod
    def delete_by_id(self, _id: str) -> str:
        pass

    @abc.abstractmethod
    def get_all_debts(self, open_debts) -> List[Debt]:
        pass
