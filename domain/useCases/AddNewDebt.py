from uuid import uuid4
from domain.entities import Date, Debt, PayableMonth
from domain.repositories import DebtRepository

class AddNewDebt:
    
    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, description:str, part_value:float, total_parts:int, start_date:dict, paid_parts:int) -> Debt:
        total_value = part_value * total_parts
        remaining_parts = total_parts - paid_parts
        remaining_value = remaining_parts*part_value
        
        months = []
        year = start_date['year']
        month = start_date['month']

        for _ in range(total_parts):
            date = Date(year = year,month=month)
            months.append(PayableMonth(date=date))

            next_month = date.get_next_month()
            month = next_month['month']
            year = next_month['year']

        for i in range(paid_parts):
            months[i].pay()

        new_debt = Debt(str(uuid4()),
                        description, 
                        part_value,
                        total_parts,
                        months,
                        total_value,
                        paid_parts,
                        remaining_parts,
                        remaining_value)

        return self.debt_repository.add(new_debt._id,
                                        new_debt._description, 
                                        new_debt._part_value,
                                        new_debt._total_parts,
                                        new_debt._months,
                                        new_debt._total_value,
                                        new_debt._paid_parts,
                                        new_debt._remaining_parts,
                                        new_debt._remaining_value)








