''' This files handles database connection for the program '''
import os
import pymongo

from src.logging.logger import get_logger

_log = get_logger(__name__)

<<<<<<< HEAD
try:
    _mongo = pymongo.MongoClient(os.getenv('MONGO_URI_PJ3'))
    _db = _mongo.mongo_csm
except:
    _log.error('Could not connect to database.')
    raise
=======
class SingletonMeta(type):
    ''' This will enforce the singleton design pattern on the DatabaseConnection class '''

    _instances = {}

    def __call__(cls, *args, **kwargs):
        ''' This function will ensure that every initialized object of a class refers to the same
        instance of the class '''
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    ''' This is the singleton object that handles all database connection and collection
    references '''
    def __init__(self):
        ''' This is the constructor. It connects to the database then creates references to the
        collections that it should have '''
        try:
            self._mongo = pymongo.MongoClient(os.getenv('MONGO_URI_PJ3'))
            self._db = self._mongo.mongo_csm
            self._swot = self._db['swot']
            self._associates = self._db['associates']
        except:
            _log.error('Could not connect to database.')
            raise

    def get_swot_collection(self):
        ''' This is a getter for the swot collection '''
        return self._swot

    def get_associates_collection(self):
        ''' This is a getter for the associates collection '''
        return self._associates
>>>>>>> 1dacb4003024fc52d1539a1405c83bd10a327e20
