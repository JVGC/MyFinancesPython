from uuid import uuid4
from domain.useCases.PayDebtPart import PayDebtPart
from infra.repositories import DebtRepositoryMemory, DebtRepositoryMongo
import unittest


class TestPayDebtPart(unittest.TestCase):

    def test_pay_debt_part_success(self):
        debt_repository_mongo = DebtRepositoryMongo()

        debt_data = debt_repository_mongo.add(_id = str(uuid4()),
                                                description =  "test debt",
                                                part_value =  135,
                                                total_parts =  10,
                                                start_date =  3,
                                                paid_parts =  0,
                                                total_value = 1350,
                                                remaining_parts= 10,
                                                remaining_value= 1350)

        pay_debt_part = PayDebtPart(debt_repository_mongo)


        paid_debt = pay_debt_part.execute(debt_data._id)

        assert paid_debt._paid_parts == 1
        assert paid_debt._remaining_parts == 9
        assert paid_debt._remaining_value == 1215

    def test_pay_debt_part_already_paid(self):
        debt_repository_mongo = DebtRepositoryMongo()

        debt_data = debt_repository_mongo.add(_id = str(uuid4()),
                                                description =  "test debt",
                                                part_value =  135,
                                                total_parts =  10,
                                                start_date =  3,
                                                paid_parts =  10,
                                                total_value = 1350,
                                                remaining_parts= 0,
                                                remaining_value= 0)

        pay_debt_part = PayDebtPart(debt_repository_mongo)

        with self.assertRaises(Exception) as context:
            pay_debt_part.execute(debt_data._id)

        assert str(context.exception) == 'Error: Esse débito já está totalmente pago'