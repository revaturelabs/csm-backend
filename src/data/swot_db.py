''' File to define SWOT MongoDB operations. '''
import pymongo

from src.data.data import DatabaseConnection
from src.data.associates_db import update_associate_swot
from src.models.swot import SWOT

from src.logging.logger import get_logger

_log = get_logger(__name__)

_swot = DatabaseConnection().get_swot_collection()

def create_swot(query_key: str, query_val: str, new_swot: dict):
    ''' Creates a SWOT for am associate in the database. Query Key should be either
    salesforce_id or email '''
    if query_key in ['salesforce_id', 'email']:
        query_string = {query_key: query_val}
        # Make swot keys all lowercase so that the request is case insensetive, and so it
        # validates correctly
        uncased_swot = {key.lower(): val for key, val in new_swot.items()}
        required_fields = ['Strengths', 'Weaknesses', 'Opportunities', 'Threats', 'Notes', 'date_created', 'author']
        _log.debug(uncased_swot)
        # Verify that all the keys of the uncased_swot dict are in the required fields list
        if all(field in new_swot for field in required_fields):
            try:
                _log.debug('setting swot field')
                new_swot['_id'] = _get_id()
                swot_final = SWOT.from_dict(new_swot)
                update_associate_swot(query_string, swot_final.to_dict())
                doc = swot_final.to_dict()
                _log.debug(swot_final)
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

def _get_id():
    '''Retrieves the next id in the database and increments it'''
    return _swot.find_one_and_update({'_id': 'UNIQUE_COUNT'},
                                     {'$inc': {'count': 1}},
                                     return_document=pymongo.ReturnDocument.AFTER)['count']
