
from domain.repositories import DebtRepository
from domain.useCases import AddNewDebt, GetDebtById, PayDebtPart, UpdateDebtDescription, DeleteDebtById
from infra.controllers.contracts.http import HttpRequest, HttpResponse
from infra.controllers.errors import InvalidFieldsError, NotFoundError

class DebtController:

    def __init__(self, debt_repository: DebtRepository) -> None:

        self.debt_repository = debt_repository

    def add_new_debt(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body

        description = body.get('description')
        part_value = body.get('part_value')
        total_parts = body.get('total_parts')
        start_date = body.get('start_date')
        paid_parts = body.get('paid_parts')

        add_new_debt = AddNewDebt(self.debt_repository)

        response = add_new_debt.execute(description,
                                        part_value,
                                        total_parts,
                                        start_date,
                                        paid_parts)

        if response.is_err():
            return InvalidFieldsError(field=response.err().entity, reason=response.err().reason)

        new_debt = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                                'debt': new_debt.to_dict()
                            }, 200)
    def get_debt_by_id(self, http_request: HttpRequest) -> HttpResponse:
        get_debt_by_id = GetDebtById(self.debt_repository)

        params = http_request.params
        response = get_debt_by_id.execute(params.get('debt_id'))

        if response.is_err():
            return NotFoundError(response.err().message)

        debt = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                                'debt': debt.to_dict()
                            }, 200)

    def pay_debt_part(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body
        debt_id = body.get('debt_id')

        pay_debt_part = PayDebtPart(self.debt_repository)

        paid_debt = pay_debt_part.execute(debt_id)

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                                'debt': paid_debt.to_dict()
                            }, 200)

    def update_debt_description(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body
        params = http_request.params
        new_description = body.get('description')

        update_debt_description = UpdateDebtDescription(self.debt_repository)

        response = update_debt_description.execute(params.get('debt_id'), new_description)

        if response.is_err():
            return NotFoundError(response.err().message)

        debt = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                                'debt': debt.to_dict()
                            }, 200)
    
    def delete_debt_by_id(self, http_request: HttpRequest) -> HttpResponse:
        
        params = http_request.params
        
        delete_debt_by_id = DeleteDebtById(self.debt_repository)

        response = delete_debt_by_id.execute(params.get('debt_id'))

        if response.is_err():
            return NotFoundError(response.err().message)

        deleted_id = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                                'debt_id': deleted_id
                            }, 200)