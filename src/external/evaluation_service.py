'''this module is to pull from Caliber assessment-controller
   grade-controller and note-controller'''

import requests, os, json

from src.testing_logging.logger import get_logger

_log = get_logger(__name__)

EXTERNAL_API = os.getenv('EXTERNAL_API')
_log.debug(EXTERNAL_API)
_caliber = EXTERNAL_API + 'evaluation'
_log.debug(_caliber)

def get_associate_spider_data(batchId, associateEmail):
    '''this method hits the Caliber evaluation-controller
       /grades/reports/{batchId}/spider/{associateEmail} with a get request 
       to get spider graph information about an associate'''
    url = '/grades/reports/' + batchId + '/spider/' + associateEmail
    return requests.get(_caliber + url).text
