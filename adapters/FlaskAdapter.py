
from flask import request, g, jsonify
from functools import wraps
from infra.controllers.contracts import HttpRequest
class FlaskAdapter:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def create(fn):

        @wraps(fn)
        def decorated_function(**kwargs):

            http_request = HttpRequest(body=request.get_json(),
                                        query=request.args,
                                        params=kwargs)

            http_response = fn(http_request)
            return jsonify(http_response.body), http_response.status_code

        return decorated_function