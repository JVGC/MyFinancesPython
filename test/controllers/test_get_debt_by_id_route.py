import unittest
from infra.controllers.contracts.http import HttpRequest

from infra.controllers.DebtController import DebtController
from infra.controllers.errors import NotFoundError
from infra.repositories import DebtRepositoryMongo

class TestGetDebtByIdRoute(unittest.TestCase):

    def test_success(self):
        
        debt_repository_mongo = DebtRepositoryMongo()
        debt_controller = DebtController(debt_repository_mongo)

        request = HttpRequest(params={'id': '123'})
        http_response = debt_controller.add_new_debt(request)

        assert http_response.status_code == 200
        assert http_response.body['debt']['description'] == request.body['description']

    def test_debt_not_found(self):
        debt_repository_mongo = DebtRepositoryMongo()
        debt_controller = DebtController(debt_repository_mongo)

        request = HttpRequest(params={'id': '123'})
        http_response = debt_controller.get_debt_by_id(request)

        assert http_response.status_code == 404

        assert isinstance(http_response, NotFoundError)


