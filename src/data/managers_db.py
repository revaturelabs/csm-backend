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
