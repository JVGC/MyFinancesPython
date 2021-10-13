

from domain.repositories import DebtRepository


class DeleteDebtById:
    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, debt_id):

        found_debt = self.debt_repository.get_by_id(debt_id)

        if not found_debt:
            raise Exception("Error: Débito não encontrado")

        return self.debt_repository.delete_by_id(debt_id)