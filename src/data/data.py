''' This files handles the database functionality for the program '''

import pymongo, os
from src.models.associates import Associate

from src.models.swot import SWOT

from src.testing_logging.logger import get_logger

_log = get_logger(__name__)

# MONGO_URI_PJ3 = os.getenv('MONGO_URI_PJ3')
# mongo = pymongo.MongoClient(MONGO_URI_PJ3)
try:
    db = pymongo.MongoClient(os.environ.get('MONGO_URI')).mongo_csm
except:
    _log.exception('Could not connect to Mongo')
    raise

# db = mongo.mongo_csm
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
                _log.debug('setting swot field')
                update_string = {"$set": {"swot": new_swot}} # Note: May be appended instead
                doc = associates.find_one_and_update(query_string, update_string, 
                                                     return_document=pymongo.ReturnDocument.AFTER)
                _log.debug(doc)
            except Exception as err:
                _log.error(err)
                _log.debug('error with updating')
                doc = 'Could not update'
        else:
            _log.debug('swot is wrong')
            doc = 'Invalid SWOT'
    else:
        _log.debug('query is wrong')
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

def get_associate_batch_id(query_dict):
    '''Takes in a query dict of the associate's email and returns the batch_id'''
    associate = associates.find(query_dict)
    batch_id = []
    for i in associate:
        batch_id.append(i)
    batch_id = batch_id[0]
    batch_id = batch_id['batch_id']
    return batch_id

if __name__=="__main__":
    associates.drop()
    new_associate = Associate(sf_id="SF-8507", 
                              email="mock12.associate1b4ee47b-6d18-4c5f-bada-808f1eaf469d@mock.com", 
                              batch_id="TR-1649",
                              manager_id="manager",
                              end_date="2020-05-13")
    new_associate.__dict__['_id']='testId'
    Associate.from_dict(new_associate.__dict__)
    create_associate(new_associate)

    new_swot =  SWOT()
    _log.debug(new_swot)
    new_swot.add_swot_item('strengths', 'strengths test')
    new_swot.add_swot_item('strengths', 'strengths test 2')
    new_swot.add_swot_item('weaknesses', 'weaknesses test')
    new_swot.add_swot_item('weaknesses', 'weaknesses test 2')
    new_swot.add_swot_item('opportunities', 'opportunities test')
    new_swot.add_swot_item('opportunities', 'opportunities test 2')
    new_swot.add_swot_item('threats', 'threats test')
    new_swot.add_swot_item('threats', 'threats test 2')
    create_swot('salesforce_id', 'SF-8507', new_swot.__dict__)
