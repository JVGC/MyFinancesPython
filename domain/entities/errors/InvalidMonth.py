class InvalidMonth:
    def __init__(self, avaiable_months) -> None:

        self.message = 'Mês Inválido'
        self.entity = 'Month'
        self.reason = f"Month deveria estar entre os seguintes meses disponíveis: {avaiable_months}"