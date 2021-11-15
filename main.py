from infra.http.flask import FlaskApi
from infra.repositories.DebtRepositoryMongo import DebtRepositoryMongo

debt_repository_mongo = DebtRepositoryMongo()
flask_server = FlaskApi(debt_repository_mongo)

flask_server.run()
