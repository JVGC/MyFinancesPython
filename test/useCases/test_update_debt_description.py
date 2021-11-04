from uuid import uuid4
from domain.useCases.UpdateDebtDescription import UpdateDebtDescription
from domain.useCases.errors.DebtNotFound import DebtNotFound
from infra.repositories import DebtRepositoryMemory, DebtRepositoryMongo
import unittest

from utils import result

class TestUpdateDebtDescription(unittest.TestCase):

    def test_success(self):
        debt_repository_mongo = DebtRepositoryMongo()
        debt_data = debt_repository_mongo.add(_id = str(uuid4()),
                                                description =  "test debt",
                                                part_value =  135.0,
                                                total_parts =  10,
                                                start_date =  {
                                                    'year': 2019,
                                                    'month': 4
                                                },
                                                paid_parts =  0,
                                                total_value = 1350.0,
                                                remaining_parts= 10,
                                                remaining_value= 1350.0)

        update_debt_description = UpdateDebtDescription(debt_repository_mongo)

        result = update_debt_description.execute(id = debt_data.id, description= 'testando update')

        assert result.is_ok() == True

        assert result.ok().description == 'testando update'

    def test_debt_not_found(self):

        debt_repository_mongo = DebtRepositoryMongo()
        
        update_debt_description = UpdateDebtDescription(debt_repository_mongo)

        result = update_debt_description.execute(id = '123', description= 'testando update')

        assert result.is_err() == True

        assert isinstance(result.err(), DebtNotFound)

