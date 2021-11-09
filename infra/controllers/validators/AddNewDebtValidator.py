from infra.controllers.contracts.http import HttpRequest
from cerberus import Validator
from infra.controllers.validators.ports.CerberusErrors import CerberusErrors

from utils.result import Error, Ok, Result

class AddNewDebtValidator:

    def __init__(self) -> None:
        
        self.schema = {
            'description': {'type': 'string', 'required': True},
            'part_value': {'type': 'number', 'required': True},
            'total_parts': {'type': 'integer', 'required': True},
            'paid_parts': {'type': 'integer', 'required': True},
            'start_date': {'type': 'dict', 'required': True, 'schema':{
                'month':{
                    'type': 'integer', 'required': True
                },
                'year': {
                    'type': 'integer', 'required': True
                }
            }},
        }

        self.validator = Validator(self.schema)

    def validate(self, http_request: HttpRequest) -> Result[HttpRequest, CerberusErrors]:
        is_valid = self.validator.validate(http_request.body)

        if not is_valid:
            return Error(self.validator.errors)
        
        return Ok(http_request) 

