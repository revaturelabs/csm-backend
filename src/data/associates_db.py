''' File to define Associate MongoDB operations. '''
import pymongo

from src.data.data import _db

from src.models.associates import Associate

from src.logging.logger import get_logger

_log = get_logger(__name__)

_associates = _db['associates']

def create_associate(new_associate: Associate):
    '''Creates a new associate in the database'''
    _associates.insert_one(new_associate.to_dict())

def read_all_associates():
    '''Returns all associates'''
    return _associates.find({})

def read_all_associates_by_query(query_dict):
    '''Takes in a query_dict and returns a list of info based on that query'''
    return list(_associates.find(query_dict))

def read_one_associate_by_query(query_dict):
    '''Takes in an associate query dict and returns one associate matching query.'''
    return _associates.find_one(query_dict)

def update_associate_swot(query_dict, swot_id):
    '''Takes in a associate query_dict, a swot, and appends a swot_id'''
    try:
        _associates.update_one(query_dict, {'$append': {'swot_id': swot_id}})
        op_success = True
        _log.info('Successfully updated associate information.')
    except:
        op_success = False
        _log.info('Failed to update associate information.')
    return op_success

def assignment_counter():
    ''' This will return a list of dicts. The dicts will have an _id field, which will be the 
    manager id, and then a 'count' field, which will contain the number of associates that they are
    assigned to. '''
    return list(associates.aggregate([{
        '$group': { '_id': '$manager_id', 'count': {'$sum': 1} }
    }]))

def get_associate_batch_id(query_dict):
    '''Takes in a query dict of the associate's email and returns the batch_id'''
    associate = _associates.find(query_dict)
    batch_id = []
    for i in associate:
        batch_id.append(i)
    batch_id = batch_id[0]
    batch_id = batch_id['batch_id']
    return batch_id

def _get_id():
    '''Retrieves the next id in the database and increments it'''
    return _associates.find_one_and_update({'_id': 'UNIQUE_COUNT'},
                                           {'$inc': {'count': 1}},
                                           return_document=pymongo.ReturnDocument.AFTER)['count']
