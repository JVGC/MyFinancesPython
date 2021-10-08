from domain.repositories import DebtRepository

class PayDebtPart:

    def __init__(self, debt_repository: DebtRepository):
        self.debt_repository = debt_repository

    def execute(self, id):
        debt = self.debt_repository.get_by_id(id)
        # print(type(debt))
        if debt.is_paid():
            raise Exception('Error: Esse débito já está totalmente pago')

        debt._paid_parts +=1
        debt._remaining_parts -=1

        debt._remaining_value = debt._remaining_parts * debt._part_value       

        paid_debt = self.debt_repository.pay_debt_part(id, debt._paid_parts, debt._remaining_parts, debt._remaining_value)

        return paid_debt