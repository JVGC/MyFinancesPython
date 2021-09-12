from uuid import uuid4
from domain.useCases.PayDebtPart import PayDebtPart
from infra.repositories import DebtRepositoryMemory
import unittest


class TestPayDebtPart(unittest.TestCase):

    def test_pay_debt_part_success(self):
        debt_repository_memory = DebtRepositoryMemory()

        debt_data = debt_repository_memory.add(_id = str(uuid4()),
                                                description =  "test debt",
                                                part_value =  135,
                                                total_parts =  10,
                                                start_date =  3,
                                                paid_parts =  0,
                                                total_value = 1350,
                                                remaining_parts= 10,
                                                remaining_value= 1350)

        pay_debt_part = PayDebtPart(debt_repository_memory)


        paid_debt = pay_debt_part.execute(debt_data._id)

        assert paid_debt._paid_parts == 1