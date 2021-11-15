from domain.repositories import DebtRepository
from domain.useCases import AddNewDebt
from infra.controllers.contracts import HttpRequest, HttpResponse
from infra.controllers.contracts.ValidatorDecorator import validate
from infra.controllers.errors import InvalidFieldsError
from infra.controllers.validators import AddNewDebtValidator


class AddNewDebtOperator:

    def __init__(self, debt_repository: DebtRepository) -> None:
        self.debt_repository = debt_repository

    @validate(AddNewDebtValidator())
    def operate(self, http_request: HttpRequest) -> HttpResponse:

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
            return InvalidFieldsError(
                errors={response.err().entity: response.err().reason})

        new_debt = response.ok()

        return HttpResponse({'message': 'Requisição Executada com sucesso',
                             'debt': new_debt.to_dict()
                             }, 200)
