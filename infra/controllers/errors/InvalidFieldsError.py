from infra.controllers.contracts.http import HttpResponse


class InvalidFieldsError(HttpResponse):

    def __init__(self, errors: dict) -> None:
        status_code = 400
        self.message = 'Dados Inválidos'

        body = {
            'message': self.message,
            'errors': errors
        }

        super().__init__(body, status_code)
