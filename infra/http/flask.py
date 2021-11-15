import os

from adapters import FlaskAdapter
from flask_cors import CORS
from infra.controllers.operators.debt import *
from infra.http.FlaskRoutes import FlaskRoutes

from flask import Blueprint, Flask


class FlaskApi:

    def __init__(self, debt_repository: DebtRepository):

        self.APP = Flask(__name__)
        self.API = Blueprint('api', __name__)
        CORS(self.APP)
        self.APP.secret_key = os.urandom(24)
        self.APP.register_blueprint(self.API, url_prefix='/api')
        self.debt_repository = debt_repository

        routes = FlaskRoutes(self.debt_repository).get_routes()

        self._configure_routes(routes)

    def _configure_routes(self, routes):

        self.routes = routes
        for route in self.routes:
            self.APP.add_url_rule(route['url'], endpoint=route['url'],
                                  view_func=FlaskAdapter.create(
                route['operation']), methods=route['methods'])

    def run(self):
        self.APP.run(host='0.0.0.0', port=5000,
                     threaded=True, use_reloader=True)
