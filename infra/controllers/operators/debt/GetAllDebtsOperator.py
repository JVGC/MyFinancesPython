from domain.repositories import DebtRepository
from domain.useCases import GetAllDebts
from infra.controllers.contracts import HttpRequest, HttpResponse


class GetAllDebtsOperator:

    def __init__(self, debt_repository: DebtRepository) -> None:
        self.debt_repository = debt_repository

    def operate(self, http_request: HttpRequest) -> HttpResponse:
        get_all_debts = GetAllDebts(self.debt_repository)

        response = get_all_debts.execute()

        found_debts = response.ok()

        return HttpResponse(body={
            'message': 'Requisição Executada com sucesso',
            'debts': [debt.to_dict() for debt in found_debts]
        }, status_code=200)
