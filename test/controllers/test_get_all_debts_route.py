import unittest

from domain.useCases import AddNewDebt, DeleteDebtById
from infra.controllers.contracts.http import HttpRequest
from infra.controllers.operators.debt import GetAllDebtsOperator
from infra.repositories import DebtRepositoryMongo


class TestGetAllDebtsRoute(unittest.TestCase):

    def setUp(self) -> None:
        self.added_ids = []
        self.debt_repository = DebtRepositoryMongo()

    def test_success(self):

        get_all_debts_operator = GetAllDebtsOperator(self.debt_repository)

        add_new_debt = AddNewDebt(self.debt_repository)
        for i in range(10):

            result = add_new_debt.execute(description="test debt",
                                          part_value=135.0,
                                          total_parts=10,
                                          start_date_data={
                                              'year': 2021,
                                              'month': 4
                                          },
                                          paid_parts=0)
            self.added_ids.append(result.ok().id)

        request = HttpRequest()

        http_response = get_all_debts_operator.operate(request)

        assert http_response.status_code == 200

        assert len(http_response.body['debts']) == 10

    def tearDown(self) -> None:
        delete_debt_by_id = DeleteDebtById(self.debt_repository)
        for id in self.added_ids:
            deleted_id = delete_debt_by_id.execute(id)
