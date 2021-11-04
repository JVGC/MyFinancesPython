class InvalidType:
    def __init__(self, entity:str, expected_type, received_type) -> None:

        self.message = 'Tipo Inválido.'
        self.entity = entity

        self.reason = f"Expected type: {expected_type} : Receveid_type: {received_type}"


    def __str__(self) -> str:
        return f"{self.message} {self.entity} -> Tipo esperado: {self.expected_type} : Tipo recebido: {self.received_type}"
