'''this module is used to pull information from the
    Caliber associate-controller and Caliber batch-controller'''
import os
import requests

from src.logging.logger import get_logger

_log = get_logger(__name__)

_caliber = os.getenv('EXTERNAL_API') + 'training'


def batch_current():
    '''this method hits the Caliber batch-controller
       /batch/current with a get request to get information about all current
       batches'''
<<<<<<< HEAD
    return requests.get(_caliber + '/batch/current').json()
=======
    return requests.get(_caliber + '/batch/current').text

def get_batch_by_id(batch_id):
    ''' this method hits caliber batch-controller
        /batch/{batchId} with a get request to get information on specific batches'''
    return requests.get(_caliber + '/batch/' + batch_id).json()
>>>>>>> fa8d6c02c938522d25d09ac11d2429d8da4a79ed
