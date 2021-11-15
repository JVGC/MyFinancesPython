import unittest

from infra.controllers.contracts.http import HttpRequest
from infra.controllers.validators.AddNewDebtValidator import \
    AddNewDebtValidator


class TestAddNewDebtValidator(unittest.TestCase):

    def test_correct_payload(self):

        add_new_debt_validator = AddNewDebtValidator()
        http_request = HttpRequest(body={
            'description': 'test_add_new_debt_route',
            'part_value': 18.9,
            'total_parts': 15,
            'start_date': {
                'year': 2020,
                'month': 8
            },
            'paid_parts': 10
        })

        valid_or_error = add_new_debt_validator.validate(http_request)

        assert valid_or_error.is_ok() is True

    def test_total_parts_float(self):

        add_new_debt_validator = AddNewDebtValidator()
        http_request = HttpRequest(body={
            'description': 'test_add_new_debt_route',
            'part_value': 18,
            'total_parts': 15.0,
            'start_date': {
                'year': 2020,
                'month': 8
            },
            'paid_parts': 10
        })

        valid_or_error = add_new_debt_validator.validate(http_request)

        assert valid_or_error.is_err() is True

        errors = valid_or_error.err()

        assert isinstance(errors, dict)

        assert 'total_parts' in errors.keys()

    def test_missing_fields(self):

        add_new_debt_validator = AddNewDebtValidator()
        http_request = HttpRequest(body={
            'description': 'test_add_new_debt_route',
            'part_value': int(0),
            'start_date': {
                'year': 2020,
            }
        })

        valid_or_error = add_new_debt_validator.validate(http_request)

        assert valid_or_error.is_err() is True

        errors = valid_or_error.err()

        assert isinstance(errors, dict)

        assert 'paid_parts' in errors.keys()
        assert 'total_parts' in errors.keys()
        assert 'start_date' in errors.keys()
        assert 'month' in errors['start_date'][0].keys()

    def test_unknown_fields(self):

        add_new_debt_validator = AddNewDebtValidator()
        http_request = HttpRequest(body={
            'description': 'test_add_new_debt_route',
            'part_value': 18,
            'total_parts': 15.0,
            'start_date': {
                'year': 2020,
                'month': 8,
                'eu_tambem_nao': [100]
            },
            'paid_parts': 10,
            'eu_nao_existo': '100'
        })

        valid_or_error = add_new_debt_validator.validate(http_request)

        assert valid_or_error.is_err() is True

        errors = valid_or_error.err()

        assert isinstance(errors, dict)

        assert 'eu_nao_existo' in errors.keys()
        assert 'start_date' in errors.keys()
        assert 'eu_tambem_nao' in errors['start_date'][0].keys()
