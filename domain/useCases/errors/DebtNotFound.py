from .UseCaseError import UseCaseError
class DebtNotFound(UseCaseError):
    def __init__(self) -> None:

        message = 'Débito não encontrado'
        status = 'debt_not_found'

        super().__init__(message, status)