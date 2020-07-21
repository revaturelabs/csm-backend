# from src.data.data import _db

# from src.logging.logger import get_logger

# _log = get_logger(__name__)

# _managers = _db['managers']

# def manager_login(manager_email):
#     '''A function that takes in an email and return the corresponding staging manager if one exists'''
#     query_dict = {'_id': manager_email}
#     manager = _managers.find_one(query_dict)
#     # manager.pop('ObjectId')
#     return manager
