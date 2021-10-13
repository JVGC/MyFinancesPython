import unittest
from uuid import uuid4
from domain.useCases import DeleteDebtById
from domain.useCases.AddNewDebt import AddNewDebt
from infra.repositories import DebtRepositoryMongo


class TestDeleteDebtById(unittest.TestCase):

    def test_delete_debt_by_id_success(self):
        debt_repository_mongo = DebtRepositoryMongo()

        add_new_debt = AddNewDebt(debt_repository_mongo)
        debt_data = add_new_debt.execute(description =  "test debt",
                                        part_value =  135,
                                        total_parts =  10,
                                        start_date =  {
                                            "month": "8",
		                                    "year": 2021
                                        },
                                        paid_parts =  0).to_dict()


        delete_debt_by_id = DeleteDebtById(debt_repository_mongo)

        deleted_id = delete_debt_by_id.execute(debt_data['_id'])

        assert deleted_id == debt_data['_id']