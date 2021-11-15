from domain.repositories import DebtRepository
from infra.controllers.operators.debt import *


class FlaskRoutes:

    def __init__(self, debt_repository: DebtRepository) -> None:
        self.debt_repository = debt_repository
        self.routes = [{
            'url': '/debt/add',
            'operation': AddNewDebtOperator(self.debt_repository).operate,
            'methods': ['POST']
        }, {
            'url': '/debt/pay',
            'operation': PayDebtPartOperator(self.debt_repository).operate,
            'methods': ['PUT']
        }, {
            'url': '/debt/description/<debt_id>',
            'operation': UpdateDebtDescriptionOperator(
                self.debt_repository).operate,
            'methods': ['PUT']
        }, {
            'url': '/debt/<debt_id>',
            'operation': GetDebtByIdOperator(self.debt_repository).operate,
            'methods': ['GET']
        }, {
            'url': '/debt/delete/<debt_id>',
            'operation': DeleteDebtByIdOperator(self.debt_repository).operate,
            'methods': ['DELETE']
        }]

    def get_routes(self):
        return self.routes
