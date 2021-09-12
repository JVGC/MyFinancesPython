from uuid import uuid4
from domain.entities.Debt import Debt
from domain.repositories import DebtRepository

class AddNewDebt:
    
    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, description, part_value, total_parts, start_date, paid_parts):
        total_value = part_value * total_parts
        remaining_parts = total_parts - paid_parts
        remaining_value = remaining_parts*part_value
        
        new_debt = Debt(str(uuid4()),
                        description, 
                        part_value,
                        total_parts,
                        start_date,
                        total_value,
                        paid_parts,
                        remaining_parts,
                        remaining_value)

        return self.debt_repository.add(new_debt._id,
                                        new_debt._description, 
                                        new_debt._part_value,
                                        new_debt._total_parts,
                                        new_debt._start_date,
                                        new_debt._total_value,
                                        new_debt._paid_parts,
                                        new_debt._remaining_parts,
                                        new_debt._remaining_value)








