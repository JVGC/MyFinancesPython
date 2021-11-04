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

        new_debt_id = self.db['debts'].insert_one(new_debt).inserted_id
        
        new_debt_data = self.db['debts'].find_one(filter={'_id': new_debt_id})


        return self.debt_adapter.adapt(new_debt_data['_id'], 
                                new_debt_data['description'], 
                                new_debt_data['part_value'],
                                new_debt_data['total_parts'],
                                new_debt_data['start_date'],
                                new_debt_data['paid_parts'])

    def get_by_id(self, _id):

        debt = self.db['debts'].find_one(filter={'_id': _id})
        if not debt:
            return None
        return self.debt_adapter.adapt(debt['_id'], 
                                debt['description'], 
                                debt['part_value'],
                                debt['total_parts'],
                                debt['start_date'],
                                debt['paid_parts'],)

    def update_description(self, _id, description):
        self.db['debts'].update_one(filter={'_id': _id}, update={'$set':{'description': description}})

        debt = self.db['debts'].find_one(filter={'_id': _id})

        return self.debt_adapter.adapt(debt['_id'], 
                                debt['description'], 
                                debt['part_value'],
                                debt['total_parts'],
                                debt['start_date'],
                                debt['paid_parts'])

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
                                debt['paid_parts'])


    def delete_by_id(self, _id: str) -> str:
        self.db['debts'].delete_one({'_id':_id})

        return _id