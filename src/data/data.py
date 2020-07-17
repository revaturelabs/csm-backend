''' This files handles the database functionality for the program '''

import pymongo, os
from csm-backend.src.models.associates import Associate
from csm-backend.testing_logging.logger import get_logger

_log = get_logger(__name__)

MONGO_URI_PJ3 = os.getenv('MONGO_URI')
mongo = pymongo.MongoClient(MONGO_URI_PJ3)

db = mongo.mongo_csm
associates = db['associates']

def create_associate(new_associate: Associate):
    '''Creates a new associate in the database'''
    associates.insert_one(new_associate.to_dict())

def read_all_associates():
    '''Returns all associates'''
    return associates.find({})

def read_all_associates_by_query(query_dict):
    '''Takes in a query_dict and returns a list of info based on that query'''
    return list(associates.find(query_dict))

def get_batches():
    '''Returns all batches from the database, these in database have been pulled
    from caliber so all are post promotion'''
    dict_list = db.batches.find()
    return [Batch.from_dict(batch) for batch in dict_list]

def create_batches(batch):
    '''Adds a batch to the mongo database'''
    _log.debug('in db')
    # _caliber.batches.insert_one(batch)
    return batch

def update_associate_swot(query_dict, swot):
    '''Takes in a swot query_dict, a swot, and updates the swot'''
    try:
        associates.update_one(query_dict, {'$set': swot})
        op_success = True
        _log.info('Successfully updated associate information.')
    except:
        op_success = False
        _log.info('Failed to update associate information.')
    return op_success

if __name__=="__main__":
    associates.drop()
