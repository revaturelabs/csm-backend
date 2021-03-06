''' Module to hold the functions that make calls to the qc-note-controller
    and the qc-category-controller '''
import os
import requests

from src.logging.logger import get_logger

_log = get_logger(__name__)
_caliber = os.getenv('EXTERNAL_API') + 'qa'

def get_note_headers(associate_id: str):
    '''This function is to get the week summary for qc notes on an associate based on a given
       associate id (sales force id)'''
    _log.info('qc_service get_note_headers called with the associate id of: %s', associate_id)
    try:
        req = requests.get(_caliber + '/notes/trainee/' + associate_id)
        return req.json()
    except:
        _log.warning('system could not process your request for note headers')


def get_qc_category(batch_id: str, week: int):
    '''this function takes a batch id and a week number and returns the topic for the week'''
    _log.info('qc_service get_qc_category called with batch: %s and week: %s', batch_id, week)
    try:
        req = requests.get(_caliber + '/category/' + batch_id + '/' + week)
        return req.json()[0]['skillCategory']
    except:
        _log.warning('system could not process your request for categories')
        return 'No Skill Provided for this QC'
