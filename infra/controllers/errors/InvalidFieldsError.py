from infra.controllers.contracts.http import HttpResponse


class InvalidFieldsError(HttpResponse):

    def __init__(self, field, reason) -> None:
        status_code = 400
        self.message = 'Dados Inválidos'

        body = {
            'message': self.message,
            'error': {
                'field': field,
                'reason': reason
            }
        }

        super().__init__(body, status_code)