from abc import abstractclassmethod


from infra.controllers.contracts import HttpRequest
from infra.controllers.validators.ports.CerberusErrors import CerberusErrors
from utils.result import Result

class PayloadValidator:
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def validate(self, http_request: HttpRequest) -> Result[HttpRequest, CerberusErrors]:
        pass