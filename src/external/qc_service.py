''' Module to hold the functions that make calls to the qc-note-controller
    and the qc-category-controller '''

import os
import requests

from src.testing_logging.logger import get_logger

_log = get_logger(__name__)
_caliber = os.getenv('EXTERNAL_API') + 'qa'

def get_note_headers(associate_id:str):
    '''This function is to get the week summery for qc notes on an associate based on a given associate id (sales force id)'''
    _log.info('qc_service get_note_headers called with the associate id of: ' + associate_id)
    try:
        r=requests.get(_caliber + '/notes/trainee/' + associate_id)
        return r.json()
    except:
        _log.warning('system could not process your request for note headers')

def get_notes(note_id:int):
    '''this function takes a note id and returns the qc note'''
    _log.info('qc_service get_notes called with the note id of: ' + note_id)
    try:
        r=requests.get(_caliber + '/notes/' + note_id)
        return r.json()
    except:
        _log.warning('system could not process your request for notes')

def get_qc_category(batch_id:str, week:int):
    '''this function takes a batch id and a week number and returns the topic for the week'''
    _log.info(f'qc_service get_qc_category called with batch: ' + batch_id + ' and week: ' + week)
    try:
        print(_caliber + '/' + batch_id + '/' + week)
        r=requests.get(_caliber + '/category/' + batch_id + '/' + week)
        return r.json()[0]['skillCategory']
    except:
        _log.warning('system could not process your request for categories')
        return 'No Skill Provided for this QC'
