import unittest

from infra.controllers.contracts.http import HttpRequest
from infra.controllers.operators.debt import AddNewDebtOperator
from infra.repositories import DebtRepositoryMongo


class TestAddNewDebtRoute(unittest.TestCase):

    def test_success(self):

        debt_repository_mongo = DebtRepositoryMongo()
        add_new_debt_operator = AddNewDebtOperator(debt_repository_mongo)

        request = HttpRequest(body={
            'description': 'test_add_new_debt_route',
            'part_value': 18.9,
            'total_parts': 15,
            'start_date': {
                'year': 2020,
                'month': 8
            },
            'paid_parts': 10
        })
        http_response = add_new_debt_operator.operate(request)

        assert http_response.status_code == 200
        assert http_response.body['debt']['description'] == request.body['description']

    def test_invalid_month(self):
        debt_repository_mongo = DebtRepositoryMongo()
        add_new_debt_operator = AddNewDebtOperator(debt_repository_mongo)

        request = HttpRequest(body={
            'description': 'test_add_new_debt_route',
            'part_value': 18.9,
            'total_parts': 15,
            'start_date': {
                'year': 2020,
                'month': 13
            },
            'paid_parts': 10
        })
        http_response = add_new_debt_operator.operate(request)

        assert http_response.status_code == 400

        assert isinstance(http_response.body['errors'], dict)
        assert 'Month' in http_response.body['errors'].keys()

    def test_invalid_payload(self):
        debt_repository_mongo = DebtRepositoryMongo()
        add_new_debt_operator = AddNewDebtOperator(debt_repository_mongo)

        request = HttpRequest(body={
            'description': 'test_add_new_debt_route',
            'part_value': 18.9,
            'total_parts': 15.5,
            'start_date': {
                'year': 2020,
                'month': 12
            },
            'not_exist': '100'
        })
        http_response = add_new_debt_operator.operate(request)

        assert http_response.status_code == 400

        assert isinstance(http_response.body['errors'], dict)
        assert 'total_parts' in http_response.body['errors'].keys()
        assert 'paid_parts' in http_response.body['errors'].keys()
        assert 'not_exist' in http_response.body['errors'].keys()
