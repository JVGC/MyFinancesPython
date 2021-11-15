import unittest
from uuid import uuid4

from domain.useCases.errors import AlreadyPaidDebt, DebtNotFound
from domain.useCases.PayDebtPart import PayDebtPart
from infra.repositories import DebtRepositoryMemory, DebtRepositoryMongo


class TestPayDebtPart(unittest.TestCase):

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

        pay_debt_part = PayDebtPart(debt_repository_mongo)

        result = pay_debt_part.execute(debt_data.id)

        self.assertTrue(result.is_ok())

        paid_debt = result.ok()

        self.assertEqual(paid_debt.paid_parts, 1)
        self.assertEqual(paid_debt.remaining_parts, 9)
        self.assertEqual(paid_debt.remaining_value, 1215)

    def test_already_paid(self):
        debt_repository_mongo = DebtRepositoryMongo()

        debt_data = debt_repository_mongo.add(_id=str(uuid4()),
                                              description="test debt",
                                              part_value=135.0,
                                              total_parts=10,
                                              start_date={
            'year': 2019,
            'month': 4
        },
            paid_parts=10,
            total_value=1350.0,
            remaining_parts=0,
            remaining_value=0.0)

        pay_debt_part = PayDebtPart(debt_repository_mongo)

        result = pay_debt_part.execute(debt_data.id)

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), AlreadyPaidDebt)

    def test_not_found(self):
        debt_repository_mongo = DebtRepositoryMongo()

        pay_debt_part = PayDebtPart(debt_repository_mongo)

        result = pay_debt_part.execute('123')

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), DebtNotFound)
