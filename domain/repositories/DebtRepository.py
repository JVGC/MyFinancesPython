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

    def update(self, 
            description=None,
            part_value=None,
            total_parts=None,
            start_date=None,
            total_value=None,
            paid_parts=None,
            remaining_parts=None,
            remaining_value=None):
        pass