from functools import wraps

from flask import request, g
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
