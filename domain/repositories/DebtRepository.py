import abc

from domain.entities.Date import Date
from domain.entities.Debt import Debt

class DebtRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def add(self,
            _id:str, 
            description:str,
            part_value:float,
            total_parts:int,
            start_date:Date,
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