'''this module is to store the calls to the manager collection'''
from src.data.data import DatabaseConnection
from src.logging.logger import get_logger

_log = get_logger(__name__)

DB = DatabaseConnection()

_managers = DB.get_managers_collection()

def manager_login(manager_email):
    '''A function that takes in an email and return the corresponding staging manager if one exists'''
    query_dict = {'_id': manager_email}
    manager = _managers.find_one(query_dict)
    return manager
def get_all_info():
    ''' This function gets all info from the managers collection'''
    return _managers.find()

def get_managers_by_batch(batch_id):
    ''' This function gets the manager associated with a batch'''
    return _managers.find_one({'batches': batch_id})