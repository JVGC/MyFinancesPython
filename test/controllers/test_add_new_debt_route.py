import unittest
from infra.controllers.contracts.http import HttpRequest

from infra.controllers.DebtController import DebtController
from infra.repositories import DebtRepositoryMongo

class TestAddNewDebtRoute(unittest.TestCase):

    def test_success(self):
        
        debt_repository_mongo = DebtRepositoryMongo()
        debt_controller = DebtController(debt_repository_mongo)

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
        http_response = debt_controller.add_new_debt(request)

        assert http_response.status_code == 200
        assert http_response.body['debt']['description'] == request.body['description']

    def test_invalid_data(self):
        debt_repository_mongo = DebtRepositoryMongo()
        debt_controller = DebtController(debt_repository_mongo)

        request = HttpRequest(body = {
            'description': 'test_add_new_debt_route',
            'part_value': 18.9,
            'total_parts': 15,
            'start_date': {
                'year': 2020,
                'month': 13
            },
            'paid_parts': 10
        })
        http_response = debt_controller.add_new_debt(request)

        assert http_response.status_code == 400


