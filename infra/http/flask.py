import os
from flask import Flask, Blueprint
from flask_cors import CORS
from infra.controllers.DebtController import DebtController
from adapters import FlaskAdapter

from infra.repositories import DebtRepositoryMongo

class FlaskApi:
    def __init__(self):

        self.APP = Flask(__name__)
        self.API = Blueprint('api', __name__)
        CORS(self.APP)
        self.APP.secret_key = os.urandom(24)
        self.APP.register_blueprint(self.API, url_prefix='/api')
        self._configure_routes()
    
    def _configure_routes(self):

        debt_controller =  DebtController(DebtRepositoryMongo())
        flask_adapter= FlaskAdapter()

        self.APP.add_url_rule('/debt/add', view_func=flask_adapter.create(debt_controller.add_new_debt), methods=['POST'])
        self.APP.add_url_rule('/debt/<debt_id>', view_func=flask_adapter.create(debt_controller.get_debt_by_id), methods=['GET'])
        self.APP.add_url_rule('/debt/pay', view_func=flask_adapter.create(debt_controller.pay_debt_part), methods=['POST'])
        self.APP.add_url_rule('/debt/description/<debt_id>', view_func=flask_adapter.create(debt_controller.update_debt_description), methods=['PUT'])
        self.APP.add_url_rule('/debt/delete/<debt_id>', view_func=flask_adapter.create(debt_controller.delete_debt_by_id), methods=['DELETE'])

    def run(self):
        self.APP.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True)

flask_server = FlaskApi()