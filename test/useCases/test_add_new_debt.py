import unittest

from domain.entities.errors.InvalidMonth import InvalidMonth
from domain.entities.errors.InvalidType import InvalidType
from domain.useCases import AddNewDebt
from infra.repositories import DebtRepositoryMemory, DebtRepositoryMongo


class TestAddNewDebt(unittest.TestCase):

    def test_success(self):
        debt_repository_mongo = DebtRepositoryMongo()
        add_new_debt = AddNewDebt(debt_repository_mongo)

        result = add_new_debt.execute(description="test debt",
                                      part_value=135.0,
                                      total_parts=10,
                                      start_date_data={
                                          'year': 2021,
                                          'month': 4
                                      },
                                      paid_parts=0)

        assert result.is_ok() is True
        assert result.ok().description == "test debt"

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

        assert result.is_err() is True
        assert isinstance(result.err(), InvalidMonth)
