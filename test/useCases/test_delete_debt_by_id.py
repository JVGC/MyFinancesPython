import unittest
from uuid import uuid4
from domain.useCases import DeleteDebtById
from domain.useCases.AddNewDebt import AddNewDebt
from domain.useCases.errors.DebtNotFound import DebtNotFound
from infra.repositories import DebtRepositoryMongo


class TestDeleteDebtById(unittest.TestCase):

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

        delete_debt_by_id = DeleteDebtById(debt_repository_mongo)

        result = delete_debt_by_id.execute(debt_data.id)

        assert result.is_ok() is True

        assert result.ok() == debt_data.id

    def test_debt_not_found(self):
        debt_repository_mongo = DebtRepositoryMongo()

        delete_debt_by_id = DeleteDebtById(debt_repository_mongo)

        result = delete_debt_by_id.execute('123')

        assert result.is_err() is True

        assert isinstance(result.err(), DebtNotFound)
