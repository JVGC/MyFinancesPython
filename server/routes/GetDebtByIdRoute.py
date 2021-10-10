from flask import jsonify

from domain.useCases import GetDebtById
from infra.repositories import DebtRepositoryMongo

def get_debt_by_id_route(debt_id):

    get_debt_by_id = GetDebtById(DebtRepositoryMongo())

    debt = get_debt_by_id.execute(debt_id)

    return jsonify({
        'message': 'Requisição Executada com sucesso',
        'debt': debt.to_dict()
    }), 200