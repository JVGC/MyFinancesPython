
from flask import request, g, jsonify
from functools import wraps

class FlaskAdapter:

    def __init__(self) -> None:
        pass
    
    
    def create(self, fn):

        @wraps(fn)
        def decorated_function(**kwargs):
            obj, status_code = fn(request.args, request.get_json(), kwargs)
            return jsonify(obj), status_code

        return decorated_function