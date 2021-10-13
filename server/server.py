
import os
from flask import Flask, Blueprint
from flask_cors import CORS

from server.routes.DeleteDebtByIdRoute import delete_debt_by_id_route
from .routes import add_new_debt_route, get_debt_by_id_route, pay_debt_part_route, update_debt_description_route, delete_debt_by_id_route


class Server:
    def __init__(self):

        self.APP = Flask(__name__)
        self.API = Blueprint('api', __name__)
        CORS(self.APP)
        self.APP.secret_key = os.urandom(24)
        self.APP.register_blueprint(self.API, url_prefix='/api')
        self._configure_routes()
    
    def _configure_routes(self):
        self.APP.add_url_rule('/debt/add', view_func=add_new_debt_route, methods=['POST'])
        self.APP.add_url_rule('/debt/<debt_id>', view_func=get_debt_by_id_route, methods=['GET'])
        self.APP.add_url_rule('/debt/pay', view_func=pay_debt_part_route, methods=['POST'])
        self.APP.add_url_rule('/debt/description/<debt_id>', view_func=update_debt_description_route, methods=['PUT'])
        self.APP.add_url_rule('/debt/delete/<debt_id>', view_func=delete_debt_by_id_route, methods=['DELETE'])

    def run(self):
        self.APP.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True)

main_server = Server()
