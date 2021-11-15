import unittest
from uuid import uuid4

from domain.entities import Date, Debt
from infra.controllers.contracts.http import HttpRequest
from infra.controllers.operators.debt import UpdateDebtDescriptionOperator
from infra.repositories import DebtRepositoryMongo


class TestUpdateDebtDescriptionOpOperatorRoute(unittest.TestCase):

    def test_success(self):
        debt_repository_mongo = DebtRepositoryMongo()

        _id = str(uuid4())

        debt_or_err = Debt.create(_id,
                                  'testing',
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

        update_debt_description_operator = UpdateDebtDescriptionOperator(
            debt_repository_mongo)
        new_description = 'new_description'

        request = HttpRequest(
            body={'description': new_description}, params={'debt_id': _id})

        response = update_debt_description_operator.operate(request)

        assert response.status_code == 200

        assert response.body['debt']['_id'] == _id
        assert response.body['debt']['description'] == new_description

    def test_debt_not_found(self):

        debt_repository_mongo = DebtRepositoryMongo()
        update_debt_description_operator = UpdateDebtDescriptionOperator(
            debt_repository_mongo)
        new_description = 'new_description'

        request = HttpRequest(body={'description': new_description}, params={
                              'debt_id': 'not_exist'})

        response = update_debt_description_operator.operate(request)

        assert response.status_code == 404

    def test_invalid_payload(self):

        debt_repository_mongo = DebtRepositoryMongo()
        update_debt_description_operator = UpdateDebtDescriptionOperator(
            debt_repository_mongo)

        request = HttpRequest(body={'description': ['new_description']}, params={
                              'debt_id': 'not_exist'})

        response = update_debt_description_operator.operate(request)

        assert response.status_code == 400
        assert 'description' in response.body['errors'].keys()
