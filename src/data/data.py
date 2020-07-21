''' This files handles database connection for the program '''
import os
import pymongo

from src.logging.logger import get_logger

_log = get_logger(__name__)

try:
    # _mongo = pymongo.MongoClient(os.getenv('MONGO_URI_PJ3'))
    _mongo = pymongo.MongoClient(os.getenv('MONGO_URI'))
    _db = _mongo.mongo_csm
except:
    _log.error('Could not connect to database.')
    raise
