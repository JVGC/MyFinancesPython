import unittest

from domain.entities import Date
from domain.entities.errors import InvalidDay, InvalidMonth
from domain.entities.errors.InvalidType import InvalidType


class TestDate(unittest.TestCase):

    def test_create_success(self):

        result = Date.create(year=2021, month=1, day=12)

        self.assertTrue(result.is_ok())
        self.assertIsInstance(result.ok(), Date)

    def test_invalid_type(self):
        result = Date.create(year='2021', month=2, day=29)

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidType)
        self.assertEqual(result.err().expected_type, int)
        self.assertEqual(result.err().received_type, str)

    def test_none_type(self):
        result = Date.create(year=None, month=2, day=29)

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidType)
        self.assertEqual(result.err().expected_type, int)
        self.assertEqual(result.err().received_type, type(None))

    def test_day_none(self):
        result = Date.create(year=2020, month=2, day=None)

        self.assertTrue(result.is_ok())
        self.assertIsInstance(result.ok(), Date)

    def test_invalid_month(self):
        result = Date.create(year=2021, month=0, day=29)

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidMonth)

        result = Date.create(year=2021, month=13, day=29)

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidMonth)

    def test_invalid_day(self):
        result = Date.create(year=2021, month=3, day=32)

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidDay)

        result = Date.create(year=2021, month=3, day=0)

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err(), InvalidDay)
