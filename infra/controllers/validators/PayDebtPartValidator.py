from cerberus import Validator

from infra.controllers.contracts.http import HttpRequest
from infra.controllers.validators.ports import PayloadValidator, CerberusErrors
from utils.result import Result, Error, Ok


class PayDebtPartValidator(PayloadValidator):
    def __init__(self) -> None:
        self.schema = {
            'debt_id': {'type': 'string', 'required': True},
        }

        self.validator = Validator(self.schema)

    def validate(self, http_request: HttpRequest) -> Result[HttpRequest, CerberusErrors]:
        is_valid = self.validator.validate(http_request.body)

        if not is_valid:
            return Error(self.validator.errors)
        
        return Ok(http_request) 