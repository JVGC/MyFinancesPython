from uuid import uuid4
from domain.useCases.GetDebtById import GetDebtById
from infra.repositories import DebtRepositoryMemory, DebtRepositoryMongo
import unittest

class TestGetDebtById(unittest.TestCase):

    def test_get_debt_by_id_success(self):
        debt_repository_mongo = DebtRepositoryMongo()
        debt_data = debt_repository_mongo.add(_id = str(uuid4()),
                                                description =  "test debt",
                                                part_value =  135,
                                                total_parts =  10,
                                                start_date =  3,
                                                paid_parts =  0,
                                                total_value = 1350,
                                                remaining_parts= 10,
                                                remaining_value= 1350)

        get_debt_by_id = GetDebtById(debt_repository_mongo)
        debt = get_debt_by_id.execute(id=debt_data._id)

        assert debt._id == debt_data._id