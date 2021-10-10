from flask import g, jsonify

from server.decorators import contextualize
from domain.useCases import PayDebtPart
from infra.repositories import DebtRepositoryMongo

@contextualize
def pay_debt_part_route():

    debt_id = g.fields.get('debt_id')

    pay_debt_part = PayDebtPart(DebtRepositoryMongo())

    paid_debt =  pay_debt_part.execute(debt_id)

    return jsonify({
        'message': 'Débito pago com sucesso',
        'debt': paid_debt.to_dict()
    }), 200


