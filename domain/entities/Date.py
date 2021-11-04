from __future__ import annotations

from typing import Union
from utils import Error
from domain.entities.errors import InvalidDay, InvalidMonth, InvalidType
from utils.result import Ok, Result



class Date:

    AVAIABLE_MONTHS = [item for item in range(1, 12)]
    AVAIABLE_DAYS = [item for item in range(1, 31)]  

    def __init__(self,
                year:int=None,
                month:str=None,
                day:int=None):

        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def create(year:int=None,
                month:str=None,
                day:int=None) -> Result[Date, Union[InvalidType, InvalidMonth, InvalidDay]]:
        
        result = Date.validate(year, month, day)

        if result.is_err():
            return Error(result.err())

        return Ok(Date(year, month, day))

    @staticmethod
    def validate(year, month, day):

        if not isinstance(year, int):
            return Error(InvalidType('Date: year',int, type(year)))

        if not isinstance(month, int):
            return Error(InvalidType('Date: month',int, type(month)))

        if day is not None and not isinstance(day, int):
            return Error(InvalidType('Date: day',int, type(day)))
        
        if month not in Date.AVAIABLE_MONTHS:
            return Error(InvalidMonth(Date.AVAIABLE_MONTHS))
        if day is not None and day not in Date.AVAIABLE_DAYS:
            return Error(InvalidDay())

        return Ok()


    def to_dict(self):
        return {
            "day": self.day,
            "month": self.month,
            "year": self.year
        }
