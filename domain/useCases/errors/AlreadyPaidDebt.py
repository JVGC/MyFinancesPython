from .UseCaseError import UseCaseError
class AlreadyPaidDebt(UseCaseError):
    def __init__(self) -> None:

        message = 'Débito já está totalmente pago '
        status = 'already_paid_debt'

        super().__init__(message, status)