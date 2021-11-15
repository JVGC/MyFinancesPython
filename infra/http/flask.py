import os

from adapters import FlaskAdapter
from flask_cors import CORS
from infra.controllers.operators.debt import *
from infra.repositories import DebtRepositoryMongo

from flask import Blueprint, Flask


class FlaskApi:

    def __init__(self):

        self.APP = Flask(__name__)
        self.API = Blueprint('api', __name__)
        CORS(self.APP)
        self.APP.secret_key = os.urandom(24)
        self.APP.register_blueprint(self.API, url_prefix='/api')
        self.debt_repository = DebtRepositoryMongo()

        self._configure_routes()

    def _configure_routes(self):

        self.routes = [{
            'url': '/debt/add',
            'operation': AddNewDebtOperator(self.debt_repository).operate,
            'methods': ['POST']
        }, {
            'url': '/debt/pay',
            'operation': PayDebtPartOperator(self.debt_repository).operate,
            'methods': ['PUT']
        }, {
            'url': '/debt/description/<debt_id>',
            'operation': UpdateDebtDescriptionOperator(self.debt_repository).operate,
            'methods': ['PUT']
        }, {
            'url': '/debt/<debt_id>',
            'operation': GetDebtByIdOperator(self.debt_repository).operate,
            'methods': ['GET']
        }, {
            'url': '/debt/delete/<debt_id>',
            'operation': DeleteDebtByIdOperator(self.debt_repository).operate,
            'methods': ['DELETE']
        }]
        for route in self.routes:
            self.APP.add_url_rule(route['url'], endpoint=route['url'], view_func=FlaskAdapter.create(
                route['operation']), methods=route['methods'])

    def run(self):
        self.APP.run(host='0.0.0.0', port=5000,
                     threaded=True, use_reloader=True)


flask_server = FlaskApi()
