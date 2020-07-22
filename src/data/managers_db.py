'''this module is to store the calls to the manager collection'''
import pymongo

from src.data.data import DatabaseConnection
from src.logging.logger import get_logger

_log = get_logger(__name__)

_managers = DatabaseConnection().get_managers_collection()



#Tims code will be below

def get_all_info():
    ''' This function gets all info from the managers collection'''
    return _managers.find()
