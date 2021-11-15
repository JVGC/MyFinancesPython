import unittest
from uuid import uuid4

from domain.entities import Date, Debt
from infra.controllers.contracts.http import HttpRequest
from infra.controllers.errors import NotFoundError
from infra.controllers.operators.debt import DeleteDebtByIdOperator
from infra.repositories import DebtRepositoryMongo
from pymongo import response


class TestDeleteDebtByIdRoute(unittest.TestCase):

    def test_success(self):

        debt_repository_mongo = DebtRepositoryMongo()
        delete_debt_by_id_operator = DeleteDebtByIdOperator(
            debt_repository_mongo)

        _id = str(uuid4())

        debt_or_err = Debt.create(_id,
                                  'testando',
                                  10.5,
                                  5,
                                  Date.create(year=2020, month=10).ok(),
                                  8)
        new_debt = debt_or_err.ok()

        _ = debt_repository_mongo.add(new_debt.id,
                                      new_debt.description,
                                      new_debt.part_value,
                                      new_debt.total_parts,
                                      new_debt.start_date.to_dict(),
                                      new_debt.total_value,
                                      new_debt.paid_parts,
                                      new_debt.remaining_parts,
                                      new_debt.remaining_value)

        request = HttpRequest(params={'debt_id': _id})
        http_response = delete_debt_by_id_operator.operate(request)
        assert http_response.status_code == 200
        assert http_response.body['debt_id'] == _id

    def test_debt_not_found(self):
        debt_repository_mongo = DebtRepositoryMongo()
        delete_debt_by_id_operator = DeleteDebtByIdOperator(
            debt_repository_mongo)

        request = HttpRequest(params={'debt_id': '123'})
        http_response = delete_debt_by_id_operator.operate(request)

        assert http_response.status_code == 404

        assert isinstance(http_response, NotFoundError)
