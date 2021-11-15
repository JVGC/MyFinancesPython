import unittest

from infra.controllers.contracts import http
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

        self.assertEqual(http_response.status_code, 200)

        added_debt = http_response.body['debt']
        self.assertEqual(added_debt['description'],
                         request.body['description'])

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

        self.assertEqual(http_response.status_code, 400)

        self.assertIsInstance(http_response.body['errors'], dict)
        self.assertIn('Month', http_response.body['errors'])

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

        self.assertEqual(http_response.status_code, 400)

        self.assertIsInstance(http_response.body['errors'], dict)

        self.assertIn('total_parts', http_response.body['errors'])
        self.assertIn('paid_parts', http_response.body['errors'])
        self.assertIn('not_exist', http_response.body['errors'])
