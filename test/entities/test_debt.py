import unittest

from domain.entities import Date, Debt
from domain.entities.errors.InvalidType import InvalidType


class TestDebt(unittest.TestCase):

    def test_create_success(self):

        result = Debt.create(
            id='123',
            description='descricao teste',
            part_value=18.95,
            total_parts=10,
            start_date=Date.create(2020, 5, 14).ok(),
            paid_parts=5
        )

        self.assertTrue(result.is_ok())
        self.assertIsInstance(result.ok(), Debt)

    def test_id_none(self):

        result = Debt.create(
            id=None,
            description='descricao teste',
            part_value=18.95,
            total_parts=10,
            start_date=Date.create(2020, 5, 14).ok(),
            paid_parts=5
        )

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidType)

    def test_invalid_type(self):
        result = Debt.create(
            id='123',
            description='descricao teste',
            part_value='18',
            total_parts=10,
            start_date=Date.create(2020, 5, 14).ok(),
            paid_parts=5
        )

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidType)
