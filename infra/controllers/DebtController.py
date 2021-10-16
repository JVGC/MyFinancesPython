from typing import Tuple
from domain.repositories import DebtRepository
from domain.useCases import AddNewDebt, GetDebtById, PayDebtPart, UpdateDebtDescription, DeleteDebtById

class DebtController:

    def __init__(self, debt_repository: DebtRepository) -> None:

        self.debt_repository = debt_repository

    def add_new_debt(self, params, body, url_params) -> Tuple[dict, int]:
        description = body.get('description')
        part_value = body.get('part_value')
        total_parts = body.get('total_parts')
        start_date = body.get('start_date')
        paid_parts = body.get('paid_parts')

        add_new_debt = AddNewDebt(self.debt_repository)

        new_debt = add_new_debt.execute(description,
                                        part_value,
                                        total_parts,
                                        start_date,
                                        paid_parts)

        return {
            'message': 'Requisição Executada com sucesso',
            'debt': new_debt.to_dict()
        }, 200

    def get_debt_by_id(self, params, body, url_params) -> Tuple[dict, int]:
        get_debt_by_id = GetDebtById(self.debt_repository)

        debt = get_debt_by_id.execute(url_params.get('debt_id'))

        return {
            'message': 'Requisição Executada com sucesso',
            'debt': debt.to_dict()
        }, 200

    def pay_debt_part(self, params, body, url_params) -> Tuple[dict, int]:
        debt_id = body.get('debt_id')

        pay_debt_part = PayDebtPart(self.debt_repository)

        paid_debt =  pay_debt_part.execute(debt_id)

        return {
            'message': 'Débito pago com sucesso',
            'debt': paid_debt.to_dict()
        }, 200

    def update_debt_description(self, params, body, url_params) -> Tuple[dict, int]:
        new_description = body.get('description')

        update_debt_description = UpdateDebtDescription(self.debt_repository)

        debt = update_debt_description.execute(url_params.get('debt_id'), new_description)

        return {
            'message': 'Requisição executada com sucesso',
            'debt': debt.to_dict()
        }, 200
    
    def delete_debt_by_id(self, params, body, url_params) -> Tuple[dict, int]:
        delete_debt_by_id = DeleteDebtById(self.debt_repository)

        deleted_id = delete_debt_by_id.execute(url_params.get('debt_id'))

        if deleted_id:
            return {
            'message': 'Requisição Executada com sucesso',
            '_id': deleted_id
        }, 200 