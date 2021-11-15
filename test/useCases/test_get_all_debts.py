import unittest
from domain.useCases import AddNewDebt, DeleteDebtById, GetAllDebts
from infra.repositories import DebtRepositoryMongo


class TestGetAllDebts(unittest.TestCase):

    def setUp(self) -> None:
        self.added_ids = []
        self.debt_repository = DebtRepositoryMongo()
        self.get_all_debts = GetAllDebts(self.debt_repository)

    def test_success(self):

        add_new_debt = AddNewDebt(self.debt_repository)
        for i in range(10):

            result = add_new_debt.execute(description="test debt",
                                          part_value=135.0,
                                          total_parts=10,
                                          start_date_data={
                                              'year': 2021,
                                              'month': 4
                                          },
                                          paid_parts=0)
            self.added_ids.append(result.ok().id)

        result = self.get_all_debts.execute()

        assert result.is_ok() == True

        assert len(result.ok()) == 10

    def test_empty_list(self):

        result = self.get_all_debts.execute()

        self.assertTrue(result.is_ok)
        self.assertEqual(len(result.ok()), 0)

    def test_open_debts(self):

        add_new_debt = AddNewDebt(self.debt_repository)
        for i in range(5):

            result = add_new_debt.execute(description="test debt",
                                          part_value=135.0,
                                          total_parts=10,
                                          start_date_data={
                                              'year': 2021,
                                              'month': 4
                                          },
                                          paid_parts=10)
            self.added_ids.append(result.ok().id)

        for i in range(5):

            result = add_new_debt.execute(description="test debt",
                                          part_value=135.0,
                                          total_parts=10,
                                          start_date_data={
                                              'year': 2021,
                                              'month': 4
                                          },
                                          paid_parts=9)
            self.added_ids.append(result.ok().id)

        result = self.get_all_debts.execute(open_debts=True)

        self.assertTrue(result.is_ok)
        self.assertEqual(len(result.ok()), 5)
        for debt in result.ok():
            self.assertFalse(debt.is_paid())

    def tearDown(self) -> None:
        delete_debt_by_id = DeleteDebtById(self.debt_repository)
        for id in self.added_ids:
            deleted_id = delete_debt_by_id.execute(id)
