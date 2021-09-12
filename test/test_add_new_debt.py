import unittest
from domain.useCases import AddNewDebt
from  infra.repositories import DebtRepositoryMemory

class TestAddNewDebt(unittest.TestCase):

    def test_add_new_debt_success(self):
        debt_repository_memory = DebtRepositoryMemory()
        add_new_debt = AddNewDebt(debt_repository_memory)

        new_debt = add_new_debt.execute(description = "test debt",
                            part_value = 135,
                            total_parts = 10,
                            start_date = 3,
                            paid_parts = 0)

        assert new_debt._description == "test debt"

if __name__ == '__main__':
    unittest.main()