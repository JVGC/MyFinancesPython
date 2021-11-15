from domain.repositories import DebtRepository
from domain.useCases import PayDebtPart
from infra.controllers.contracts import HttpRequest, HttpResponse
from infra.controllers.contracts.ValidatorDecorator import validate
from infra.controllers.errors import NotFoundError
from infra.controllers.validators import PayDebtPartValidator


class PayDebtPartOperator:

    def __init__(self, debt_repository: DebtRepository) -> None:
        self.debt_repository = debt_repository

    @validate(PayDebtPartValidator())
    def operate(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body
        debt_id = body.get('debt_id')

        pay_debt_part = PayDebtPart(self.debt_repository)

        response = pay_debt_part.execute(debt_id)

        if response.is_err():
            return NotFoundError(response.err().message)

        paid_debt = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                             'debt': paid_debt.to_dict()
                             }, 200)
