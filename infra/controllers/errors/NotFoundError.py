from infra.controllers.contracts import HttpResponse


class NotFoundError(HttpResponse):

    def __init__(self, message) -> None:
        status_code = 404
        self.message = message

        body = {
            'message': self.message
        }

        super().__init__(body, status_code)
