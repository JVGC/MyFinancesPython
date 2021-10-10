from uuid import uuid4
from domain.repositories import DebtRepository
from adapters import DebtAdapter

class DebtRepositoryMemory(DebtRepository):
    def __init__(self):
        self.debts = []
        self.debt_adapter = DebtAdapter()

    def add(self,
            _id,
            description,
            part_value,
            total_parts,
            start_date,
            total_value,
            paid_parts,
            remaining_parts,
            remaining_value):

        new_debt = {
            '_id': _id,
            'description': description,
            'part_value': part_value,
            'total_parts': total_parts,
            'start_date': start_date,
            'total_value': total_value,
            'paid_parts': paid_parts,
            'remaining_parts': remaining_parts,
            'remaining_value': remaining_value
        }
        self.debts.append(new_debt)

        

        return self.debt_adapter.adapt(new_debt['_id'], 
                                new_debt['description'], 
                                new_debt['part_value'],
                                new_debt['total_parts'],
                                new_debt['start_date'],
                                new_debt['total_value'],
                                new_debt['paid_parts'],
                                new_debt['remaining_parts'],
                                new_debt['remaining_value'])

    def get_by_id(self, _id):

        found_debt = [debt for debt in self.debts if debt['_id'] == _id]


        found_debt = found_debt[0]

        return self.debt_adapter.adapt(found_debt['_id'], 
                                found_debt['description'], 
                                found_debt['part_value'],
                                found_debt['total_parts'],
                                found_debt['start_date'],
                                found_debt['total_value'],
                                found_debt['paid_parts'],
                                found_debt['remaining_parts'],
                                found_debt['remaining_value'])


    def update_description(self, _id, description=None):
        found_debt = [debt for debt in self.debts if debt['_id'] == _id][0]
        found_debt['description'] = description


        return self.debt_adapter.adapt(found_debt['_id'], 
                                found_debt['description'], 
                                found_debt['part_value'],
                                found_debt['total_parts'],
                                found_debt['start_date'],
                                found_debt['total_value'],
                                found_debt['paid_parts'],
                                found_debt['remaining_parts'],
                                found_debt['remaining_value'])

    def pay_debt_part(self, _id, paid_parts, remaining_parts, remaining_value):
        
        found_debt = [debt for debt in self.debts if debt['_id'] == _id][0]

        found_debt['paid_parts'] = paid_parts
        found_debt['remaining_parts'] = remaining_parts,
        found_debt['remaining_value'] = remaining_value

        return self.debt_adapter.adapt(found_debt['_id'], 
                                found_debt['description'], 
                                found_debt['part_value'],
                                found_debt['total_parts'],
                                found_debt['start_date'],
                                found_debt['total_value'],
                                found_debt['paid_parts'],
                                found_debt['remaining_parts'],
                                found_debt['remaining_value'])