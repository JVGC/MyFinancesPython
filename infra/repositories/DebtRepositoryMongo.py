from pymongo import DESCENDING, ASCENDING, TEXT, MongoClient, ReturnDocument
from time import sleep,time
from uuid import uuid4
from domain.repositories import DebtRepository
from adapters import DebtAdapter

from Environment.MongoConfigs import mongo_user, mongo_password

class DebtRepositoryMongo(DebtRepository):
    def __init__(self):
        self.debts = []
        self.debt_adapter = DebtAdapter()

        client = MongoClient('mongodb+srv://'+mongo_user+':'+mongo_password+'@cluster0.ddpte.mongodb.net/MyFinances?retryWrites=true&w=majority')

        self.db = client['MyFinances']

        print('Servidor Mongo conectado!')

    def add(self,
            _id,
            description,
            part_value,
            total_parts,
            start_date,
            total_value,
            paid_parts,
            remaining_parts,
            remaining_value):

        new_debt = {
            '_id': _id,
            'description': description,
            'part_value': part_value,
            'total_parts': total_parts,
            'start_date': start_date,
            'total_value': total_value,
            'paid_parts': paid_parts,
            'remaining_parts': remaining_parts,
            'remaining_value': remaining_value
        }

        self.db['debts'].insert_one(new_debt)

        return self.debt_adapter.adapt(new_debt['_id'], 
                                new_debt['description'], 
                                new_debt['part_value'],
                                new_debt['total_parts'],
                                new_debt['start_date'],
                                new_debt['total_value'],
                                new_debt['paid_parts'],
                                new_debt['remaining_parts'],
                                new_debt['remaining_value'])
