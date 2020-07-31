'''this module is to store the calls to the manager collection'''
from src.data.data import DatabaseConnection
from src.logging.logger import get_logger

_log = get_logger(__name__)

DB = DatabaseConnection()

_managers = DB.get_managers_collection()
_associates = DB.get_associates_collection()

def manager_login(manager_email):
    '''A function that takes in an email and return the
    corresponding staging manager if one exists'''
    query_dict = {'_id': manager_email}
    manager = _managers.find_one(query_dict)
    return manager

def read_all_managers():
    ''' This function returns all of the managers '''
    managers = _managers.find({})
    return list(managers)

def assignment_counter():
    ''' This will return a list of dicts. The dicts will have an _id field, which will be the
    manager id, and then a 'count' field, which will contain the number of associates that they are
    assigned to. '''
    return list(_associates.aggregate([
        {
            '$match': {'$or': [{'status': 'Active'}, {'status': 'Benched'}]}
        },
        {
            '$group': {'_id': '$manager_id', 'count': {'$sum': 1}}
        }
    ]))

def update_batches(manager, new_batch):
    '''This will take in a manager and a new batch, updating the manager's array of batches with
    the new batch id'''
    query = {'_id': manager}
    _managers.update_one(query, {'$addToSet': {'batches': new_batch}})
    
def get_all_info():
    ''' This function gets all info from the managers collection'''
    return _managers.find()

def get_managers_by_batch(batch_id):
    ''' This function gets the manager associated with a batch'''
    return _managers.find_one({'batches': batch_id})
