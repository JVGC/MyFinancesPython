from pymongo import DESCENDING, ASCENDING, TEXT, MongoClient, ReturnDocument
from time import sleep,time
from uuid import uuid4

from pymongo.message import query, update
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

    def get_by_id(self, _id):

        debt = self.db['debts'].find_one(filter={'_id': _id})

        return self.debt_adapter.adapt(debt['_id'], 
                                debt['description'], 
                                debt['part_value'],
                                debt['total_parts'],
                                debt['start_date'],
                                debt['total_value'],
                                debt['paid_parts'],
                                debt['remaining_parts'],
                                debt['remaining_value'])

    def update_description(self, _id, description):
        self.db['debts'].update_one(filter={'_id': _id}, update={'$set':{'description': description}})

        debt = self.db['debts'].find_one(filter={'_id': _id})

        return self.debt_adapter.adapt(debt['_id'], 
                                debt['description'], 
                                debt['part_value'],
                                debt['total_parts'],
                                debt['start_date'],
                                debt['total_value'],
                                debt['paid_parts'],
                                debt['remaining_parts'],
                                debt['remaining_value'])

    def pay_debt_part(self, _id, paid_parts, remaining_parts, remaining_value):
        
        update_obj = {
            'paid_parts': paid_parts,
            'remaining_parts': remaining_parts,
            'remaining_value': remaining_value
        }
        self.db['debts'].update_one(filter={'_id': _id}, update={'$set':update_obj})

        debt = self.db['debts'].find_one(filter={'_id': _id})

        return self.debt_adapter.adapt(debt['_id'], 
                                debt['description'], 
                                debt['part_value'],
                                debt['total_parts'],
                                debt['start_date'],
                                debt['total_value'],
                                debt['paid_parts'],
                                debt['remaining_parts'],
                                debt['remaining_value'])


