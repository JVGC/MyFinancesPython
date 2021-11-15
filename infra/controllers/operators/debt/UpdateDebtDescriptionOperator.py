from domain.repositories import DebtRepository
from domain.useCases import UpdateDebtDescription
from infra.controllers.contracts import HttpRequest, HttpResponse
from infra.controllers.contracts.ValidatorDecorator import validate
from infra.controllers.errors import NotFoundError
from infra.controllers.validators import UpdateDebtDescriptionValidator


class UpdateDebtDescriptionOperator:

    def __init__(self, debt_repository: DebtRepository) -> None:
        self.debt_repository = debt_repository

    @validate(UpdateDebtDescriptionValidator())
    def operate(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        params = http_request.params
        new_description = body.get('description')

        update_debt_description = UpdateDebtDescription(self.debt_repository)

        response = update_debt_description.execute(
            params.get('debt_id'), new_description)

        if response.is_err():
            return NotFoundError(response.err().message)

        debt = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                             'debt': debt.to_dict()
                             }, 200)
