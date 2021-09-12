
import os
from flask import Flask, Blueprint, session, request, g, jsonify
from flask_cors import CORS
from .routes import add_new_debt_route


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

    def run(self):
        self.APP.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True)

main_server = Server()
