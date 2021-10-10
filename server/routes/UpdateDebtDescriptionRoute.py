from flask import g, jsonify

from server.decorators import contextualize
from domain.useCases import UpdateDebtDescription
from infra.repositories import DebtRepositoryMongo

@contextualize
def update_debt_description_route(debt_id):

    new_description = g.fields.get('description')

    update_debt_description = UpdateDebtDescription(DebtRepositoryMongo())

    debt = update_debt_description.execute(debt_id, new_description)

    return jsonify({
        'message': 'Requisição executada com sucesso',
        'debt': debt.to_dict()
    })

