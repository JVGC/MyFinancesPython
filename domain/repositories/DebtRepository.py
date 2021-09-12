import abc

class DebtRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def add(self, part_value,
            total_parts,
            start_date,
            end_date,  
            total_value,
            paid_parts,
            remaining_parts,
            remaining_value):
        pass