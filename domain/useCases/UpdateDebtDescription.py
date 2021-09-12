from domain.repositories import DebtRepository

class UpdateDebtDescription:
    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, id, description = None):

        found_debt = self.debt_repository.get_by_id(id)

        if not found_debt:
            raise Exception('Débito não encontrado')

        return self.debt_repository.update_description(id, description)