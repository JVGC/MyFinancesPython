from flask import g, jsonify

from server.decorators import contextualize
from domain.useCases import AddNewDebt
from infra.repositories import DebtRepositoryMongo

@contextualize
def add_new_debt_route():

    description = g.fields.get('description')
    part_value = g.fields.get('part_value')
    total_parts = g.fields.get('total_parts')
    start_date = g.fields.get('start_date')
    paid_parts = g.fields.get('paid_parts')

    add_new_debt = AddNewDebt(DebtRepositoryMongo())

    new_debt = add_new_debt.execute(description,
                                    part_value,
                                    total_parts,
                                    start_date,
                                    paid_parts)

    return jsonify({
        'message': 'Requisição Executada com sucesso',
        'newDebt': new_debt.to_dict()
    }), 200