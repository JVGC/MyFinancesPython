from uuid import uuid4
from domain.useCases.UpdateDebtDescription import UpdateDebtDescription
from infra.repositories import DebtRepositoryMemory
import unittest

class TestUpdateDebtDescription(unittest.TestCase):

    def test_update_debt_description_success(self):
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
        update_debt = UpdateDebtDescription(debt_repository_memory)

        updated_debt = update_debt.execute(id = debt_data._id, description= 'testando update')

        assert updated_debt._description == 'testando update'

if __name__ == '__main__':
    unittest.main()