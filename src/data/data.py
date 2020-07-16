''' This files handles the database functionality for the program '''

import pymongo, os
from src.models.associates import Associate
from src.testing_logging.logger import get_logger

_log = get_logger(__name__)

MONGO_URI_PJ3 = os.getenv('MONGO_URI_PJ3')
mongo = pymongo.MongoClient(MONGO_URI_PJ3)

db = mongo.mongo_csm
associates = db['associates']

def create_associate(new_associate: Associate):
    '''Creates a new associate in the database'''
    associates.insert_one(new_associate.to_dict())

def create_swot(query_key: str, query_val: str, new_swot: dict):
    ''' Creates a SWOT for am associate in the database. Query Key should be either
    salesforce_id or email '''
    if (query_key == "salesforce_id" or query_key == "email"):
        query_string = {query_key: query_val}
        required_fields = ['strengths', 'weaknesses', 'opportunities', 'threats', 'notes']
        if all(field in new_swot for field in required_fields):
            try:
                update_string = {"$set": {"swot": new_swot}}
                doc = associates.find_one_and_update(query_string, update_string, 
                                                     return_document=ReturnDocument.AFTER)
            except:
                doc = 'Could not update'
        else:
            doc = 'Invalid SWOT'
    else:
        doc = 'Incorrect query parameters'

    return doc

def read_all_associates():
    '''Returns all associates'''
    return associates.find({})

def read_all_associates_by_query(query_dict):
    '''Takes in a query_dict and returns a list of info based on that query'''
    return list(associates.find(query_dict))

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
