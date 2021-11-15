class InvalidType:
    def __init__(self, entity: str, expected_type, received_type) -> None:

        self.message = 'Tipo Inválido.'
        self.expected_type = expected_type
        self.received_type = received_type
        self.entity = entity

        self.reason = f"Expected type: \
                        {self.expected_type} : \
                        Receveid_type: \
                        {self.received_type}"

    def __str__(self) -> str:
        return f"{self.message} \
                {self.entity} -> Tipo esperado: {self.expected_type} \
                : Tipo recebido: {self.received_type}"
