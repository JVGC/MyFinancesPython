from domain.repositories import DebtRepository
from domain.useCases import DeleteDebtById
from infra.controllers.contracts import HttpRequest, HttpResponse
from infra.controllers.errors import NotFoundError


class DeleteDebtByIdOperator:

    def __init__(self, debt_repository: DebtRepository) -> None:
        self.debt_repository = debt_repository

    def operate(self, http_request: HttpRequest) -> HttpResponse:
        params = http_request.params

        delete_debt_by_id = DeleteDebtById(self.debt_repository)

        response = delete_debt_by_id.execute(params.get('debt_id'))

        if response.is_err():
            return NotFoundError(response.err().message)

        deleted_id = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                             'debt_id': deleted_id
                             }, 200)
