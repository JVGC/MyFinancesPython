import abc

class DebtRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def add(self, 
            description,
            part_value,
            total_parts,
            start_date,
            total_value,
            paid_parts,
            remaining_parts,
            remaining_value):
        pass

    def get_by_id(self, _id):
        pass

    def update_description(self, _id, description):
        pass
    
    def pay_debt_part(self, _id, paid_parts, remaining_parts, remaining_value):
        pass