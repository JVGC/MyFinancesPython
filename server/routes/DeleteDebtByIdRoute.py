from flask import jsonify

from domain.useCases import DeleteDebtById
from infra.repositories import DebtRepositoryMongo


def delete_debt_by_id_route(debt_id):
    delete_debt_by_id = DeleteDebtById(DebtRepositoryMongo())

    deleted_id = delete_debt_by_id.execute(debt_id)

    if deleted_id:
        return jsonify({
        'message': 'Requisição Executada com sucesso',
        '_id': deleted_id
    }), 200