from flask import g, request, jsonify
from functools import wraps
from os import stat

from domain.useCases import AddNewDebt
from infra.repositories import DebtRepositoryMemory
def contextualize(f):
    """
    Percorre todos os campos enviados através do request.get_json()

    Returns:
        - Erro se o campo estiver vazio ou se for inválido
        - Armazena os campos dentro de fields do g (contexto do flask)
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        g.fields = {}
        fields = request.get_json()
        for field in fields:
            value = fields[field]
            g.fields[field] = value
        return f(*args, **kwargs)
    return decorated_function



@contextualize
def add_new_debt_route():


    part_value = g.fields.get('part_value')
    total_parts = g.fields.get('total_parts')
    start_date = g.fields.get('start_date')
    end_date = g.fields.get('end_date')
    paid_parts = g.fields.get('paid_parts')

    add_new_debt = AddNewDebt(DebtRepositoryMemory())

    new_debt = add_new_debt.execute(part_value,
                                    total_parts,
                                    start_date,
                                    end_date,
                                    paid_parts)

    print(new_debt)

    return jsonify({
        'message': 'Funfou',
        'newDebt': new_debt
    }), 200