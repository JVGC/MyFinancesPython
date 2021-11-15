import unittest

from domain.entities.errors.InvalidMonth import InvalidMonth
from domain.entities.errors.InvalidType import InvalidType
from domain.useCases import AddNewDebt
from infra.repositories import DebtRepositoryMemory, DebtRepositoryMongo


class TestAddNewDebt(unittest.TestCase):

    def test_success(self):
        debt_repository_mongo = DebtRepositoryMongo()
        add_new_debt = AddNewDebt(debt_repository_mongo)

        result = add_new_debt.execute(description="test_debt",
                                      part_value=135.0,
                                      total_parts=10,
                                      start_date_data={
                                          'year': 2021,
                                          'month': 4
                                      },
                                      paid_parts=0)

        self.assertTrue(result.is_ok())
        self.assertEqual(result.ok().description, 'test_debt')

    def test_invalid_date(self):

        debt_repository_mongo = DebtRepositoryMongo()
        add_new_debt = AddNewDebt(debt_repository_mongo)

        result = add_new_debt.execute(description="test debt",
                                      part_value=135.0,
                                      total_parts=10,
                                      start_date_data={
                                          'year': 2021,
                                          'month': 13
                                      },
                                      paid_parts=0)

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidMonth)
