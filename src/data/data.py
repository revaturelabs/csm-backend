''' This files handles database connection for the program '''
import os
import pymongo

from src.logging.logger import get_logger

_log = get_logger(__name__)

<<<<<<< HEAD
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
        new_swot = {key.lower(): val for key, val in new_swot.items()}
        required_fields = ['strengths', 'weaknesses', 'opportunities', 'threats', 'notes']
        if all(field.lower() in new_swot for field in required_fields):
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

def assignment_counter():
    ''' This will return a list of dicts. The dicts will have an _id field, which will be the 
    manager id, and then a 'count' field, which will contain the number of associates that they are
    assigned to. '''
    return list(associates.aggregate([{
        '$group': { '_id': '$manager_id', 'count': {'$sum': 1} }
    }]))


if __name__=="__main__":
    associates.drop()
    new_associate = Associate(sf_id="SF-8507", 
                              email="mock12.associate1b4ee47b-6d18-4c5f-bada-808f1eaf469d@mock.com", 
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
    
    _log.debug(assignment_counter())
=======
try:
    _mongo = pymongo.MongoClient(os.getenv('MONGO_URI_PJ3'))
    _db = _mongo.mongo_csm
except:
    _log.error('Could not connect to database.')
    raise
>>>>>>> f6c12bdf0333a7eaf46f4743c58faf2229b1ee0d
