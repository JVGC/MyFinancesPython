class AddNewDebt:
    
    def __init__(self, debt_repository):
        self.debt_repository = debt_repository

    def execute(self, part_value, total_parts, start_date, end_date, paid_parts, remaining_parts=None):
        total_value = part_value * total_parts
        if remaining_parts == None:
            remaining_parts = total_parts - paid_parts
        else:
            if remaining_parts != total_parts - paid_parts:
                raise Exception("Erro: Numero de parcelas inválidas")

        remaining_value = remaining_parts*part_value
        new_debt = self.debt_repository.add(part_value,
                                                total_parts,
                                                start_date,
                                                end_date,  
                                                total_value,
                                                paid_parts,
                                                remaining_parts,
                                                remaining_value)

        return new_debt







