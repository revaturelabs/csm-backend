''' File to define Associate MongoDB operations. '''
import pymongo

from src.data.data import DatabaseConnection

from src.models.associates import Associate

from src.external.caliber_processing import get_new_graduates()

from src.logging.logger import get_logger

_log = get_logger(__name__)

_associates = DatabaseConnection().get_associates_collection()

def create_associate(new_associate: Associate):
    '''Creates a new associate in the database'''
    _associates.insert_one(new_associate.to_dict())

def create_scheduled_associates():
    '''Calls the processing function to get a list of associate objects'''
    associate_list = get_new_graduates()
    for associate in associate_list:
        try:
            create_associate(associate)
            _log.info('Associate added')
        except:
            _log.info("Unable to add associate; already exists")

def read_all_associates():
    '''Returns all associates'''
    return _associates.find({})

def read_all_associates_by_query(query_dict):
    ''' Takes in a query_dict and returns a list of info based on that query '''
    return list(_associates.find(query_dict))

def read_one_associate_by_query(query_dict):
    ''' Takes in an associate query dict and returns one associate matching query. '''
    return _associates.find_one(query_dict)

def update_associate_swot(query_dict, swot_id):
    ''' Takes in a associate query_dict, a swot_id, and appends the swot_id to the matching 
    associate's swot field in the database. If there are no swots in the field (i.e. the field is
    null in the database), it creates an array with the swot_id inside instead. '''
    _log.debug(query_dict)
    try:
        update_user = _associates.find_one(query_dict)
        _log.debug(update_user)
        if update_user['swot'] == None:
            _associates.update_one(query_dict, {'$set': {'swot': [swot_id]}})
        else:
            _associates.update_one(query_dict, {'$push': {'swot': swot_id}})
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
    return list(_associates.aggregate([
        {
            '$match': {'$or': [{'status': 'Active'}, {'status': 'Benched'}]}
        },
        {
            '$group': { '_id': '$manager_id', 'count': {'$sum': 1} }
        }
    ]))

def get_associate_batch_id(query_dict):
    ''' Takes in a query dict of the associate's email and returns the batch_id '''
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
