from domain.repositories import DebtRepository
from domain.useCases import GetDebtById
from infra.controllers.contracts import HttpRequest, HttpResponse
from infra.controllers.errors import NotFoundError


class GetDebtByIdOperator:

    def __init__(self, debt_repository: DebtRepository) -> None:
        self.debt_repository = debt_repository

    def operate(self, http_request: HttpRequest) -> HttpResponse:
        get_debt_by_id = GetDebtById(self.debt_repository)

        params = http_request.params
        response = get_debt_by_id.execute(params.get('debt_id'))

        if response.is_err():
            return NotFoundError(response.err().message)

        debt = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                             'debt': debt.to_dict()
                             }, 200)
