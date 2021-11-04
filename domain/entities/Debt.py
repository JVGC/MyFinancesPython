from __future__ import annotations
from typing import Union
from domain.entities.errors import InvalidType
from utils.result import E, Error, Ok, Result
from .Date import Date

class Debt:
    def __init__(self,
                id:str = None,
                description:str = None,
                part_value:float = None,
                total_parts:int = None,
                start_date: Date = None,
                paid_parts:int = None):
        
        self.id = id
        self.description = description
        self.part_value = part_value
        self.total_parts = total_parts
        self.start_date = start_date
        self.paid_parts =  paid_parts

        self.total_value = self.part_value * self.total_parts
        self.remaining_parts = self.total_parts - self.paid_parts
        self.remaining_value = self.part_value * self.remaining_parts
        

    @staticmethod
    def validate(
        id:str = None,
        description:str = None,
        part_value:float = None,
        total_parts:int = None,
        start_date: Date = None,
        paid_parts:int = None):
        
        if not isinstance(id, str):
            return Error(InvalidType('Debt: id',str, type(id)))

        if not isinstance(description, str):
            return Error(InvalidType('Debt: description',str, type(description)))
        
        if not isinstance(part_value, float):
            return Error(InvalidType('Debt: part_value',float, type(part_value)))
        
        if not isinstance(total_parts, int):
            return Error(InvalidType('Debt: total_parts',int, type(total_parts)))
        
        if not isinstance(start_date, Date):
            return Error(InvalidType('Debt: start_date',Date, type(start_date)))

        if not isinstance(paid_parts, int):
            return Error(InvalidType('Debt: paid_parts',int, type(paid_parts)))

        return Ok()


    @staticmethod
    def create(id:str = None,
                description:str = None,
                part_value:float = None,
                total_parts:int = None,
                start_date: Date = None,
                paid_parts:int = None) -> Result[Debt, Union[InvalidType]]:

        result = Debt.validate(id,
                description,
                part_value,
                total_parts,
                start_date,
                paid_parts)

        if result.is_err():
            return Error(result.err())
        
        return Ok(Debt(id,
                        description,
                        part_value,
                        total_parts,
                        start_date,
                        paid_parts))

    
    def is_paid(self):
        return self.remaining_parts == 0

    def to_dict(self):
        return {
            '_id': self.id,
            'description': self.description,
            'part_value': self.part_value,
            'total_parts': self.total_parts,
            'paid_parts': self.paid_parts,
            'remaining_parts': self.remaining_parts,
            'remaining_value': self.remaining_value,
            'start_date': self.start_date.to_dict()
        }