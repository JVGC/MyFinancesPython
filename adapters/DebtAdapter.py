from domain.entities.Debt import Debt


class DebtAdapter():

    def __init__(self):
        pass

    def adapt(self, _id, 
            description, 
            part_value,
            total_parts,
            months,
            total_value,
            paid_parts,
            remaining_parts,
            remaining_value):

        return Debt(_id,
                description,
                part_value,
                total_parts,
                months,
                total_value,
                paid_parts,
                remaining_parts,
                remaining_value)