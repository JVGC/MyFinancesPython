from domain.repositories import DebtRepository
from domain.entities import Debt

class DebtRepositoryMemory(DebtRepository):
    def __init__(self):
        pass

    def add(self,part_value,
            total_parts,
            start_date,
            end_date,  
            total_value,
            paid_parts,
            remaining_parts,
            remaining_value):

        # new_debt = Debt(part_value=part_value,
        #                 total_parts=total_parts,
        #                 start_date=start_date,
        #                 end_date=end_date,  
        #                 total_value=total_value,
        #                 paid_parts=paid_parts,
        #                 remaining_parts=remaining_parts,
        #                 remaining_value=remaining_value)

        new_debt = {
            "part_value": part_value,
            "total_parts": total_parts,
            "start_date": start_date,
            "end_date": end_date,  
            "total_value": total_value,
            "paid_parts": paid_parts,
            "remaining_parts": remaining_parts,
            "remaining_value": remaining_value
        }

        return new_debt