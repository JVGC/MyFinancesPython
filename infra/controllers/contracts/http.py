class HttpRequest:

    def __init__(self, body=None, query=None, params=None) -> None:
        self.body = body
        self.query = query
        self.params = params


class HttpResponse:

    def __init__(self, body, status_code) -> None:
        self.status_code = status_code
        self.body = body
