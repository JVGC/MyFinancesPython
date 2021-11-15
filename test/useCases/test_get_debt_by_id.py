from uuid import uuid4
from domain.useCases.GetDebtById import GetDebtById
from domain.useCases.errors.DebtNotFound import DebtNotFound
from infra.repositories import DebtRepositoryMemory, DebtRepositoryMongo
import unittest


class TestGetDebtById(unittest.TestCase):

    def test_success(self):
        debt_repository_mongo = DebtRepositoryMongo()
        debt_data = debt_repository_mongo.add(_id=str(uuid4()),
                                              description="test debt",
                                              part_value=135.0,
                                              total_parts=10,
                                              start_date={
            'year': 2019,
            'month': 4
        },
            paid_parts=0,
            total_value=1350.0,
            remaining_parts=10,
            remaining_value=1350.0)

        get_debt_by_id = GetDebtById(debt_repository_mongo)
        result = get_debt_by_id.execute(id=debt_data.id)

        assert result.is_ok() is True
        assert result.ok().id == debt_data.id

    def test_debt_not_found(self):
        debt_repository_mongo = DebtRepositoryMongo()

        get_debt_by_id = GetDebtById(debt_repository_mongo)
        result = get_debt_by_id.execute(id='123')

        assert result.is_err() is True
        assert isinstance(result.err(), DebtNotFound)
