from infra.controllers.contracts import HttpRequest
from infra.controllers.errors import InvalidFieldsError
from infra.controllers.validators.ports import PayloadValidator


def validate(validator: PayloadValidator):
    def wrapper(route):
        def controller_method(self, http_request: HttpRequest):
            is_valid_or_error = validator.validate(http_request)
            if is_valid_or_error.is_err():
                return InvalidFieldsError(errors=is_valid_or_error.err())
            return route(self, http_request)
        return controller_method
    return wrapper
