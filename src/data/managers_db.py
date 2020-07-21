from src.data.data import _db

_managers = _db['managers']

def manager_login(manager_email):
    '''A function that takes in an email and return the corresponding staging manager if one exists'''
    query_dict = {'email': manager_email}
    manager = _managers.find_one(query_dict)
    return manager
