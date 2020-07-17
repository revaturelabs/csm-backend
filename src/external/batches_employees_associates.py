'''this module is used to pull information from the 
    Caliber associate-controller and Caliber batch-controller'''

import requests, os

from src.testing_logging.logger import get_logger

_log = get_logger(__name__)

_caliber = os.getenv('EXTERNAL_API') + 'training'


def batch_current():
    '''this method hits the Caliber batch-controller
       /batch/current with a get request to get information about all current 
       batches'''
    return requests.get(_caliber + '/batch/current').text