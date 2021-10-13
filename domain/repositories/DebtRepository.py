import abc
from typing import List

from domain.entities.Date import Date
from domain.entities.Debt import Debt
from domain.entities.PayableMonth import PayableMonth

class DebtRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def add(self,
            _id:str, 
            description:str,
            part_value:float,
            total_parts:int,
            months:List[PayableMonth],
            total_value:float,
            paid_parts:int,
            remaining_parts:int,
            remaining_value:float) -> Debt:
        pass

    @abc.abstractmethod
    def get_by_id(self, _id:str) -> Debt:
        pass
    
    @abc.abstractmethod
    def update_description(self, _id:str, description:str) -> Debt:
        pass
    
    @abc.abstractmethod
    def pay_debt_part(self, _id:str, paid_parts:int, remaining_parts:int, remaining_value:float) -> Debt:
        pass