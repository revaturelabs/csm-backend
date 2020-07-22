'''this module is the driver that calls and processes from caliber'''

import json

from src.external import evaluation_service, category_service, evaluation_service, qc_service
from src.logging.logger import get_logger

_log = get_logger(__name__)

def get_qc_data(associate_id):
    '''this function gets qc data from caliber from a salesforce id'''
    notes = qc_service.get_note_headers(associate_id)
    _log.debug(qc_service.get_note_headers)
    _log.debug(notes)
    process_data = []
    for note in notes:
        if note['content']:
            content = note['content']
            score = note['technicalStatus']
            week = note['week']
            batchId = note['batchId']
            skill = qc_service.get_qc_category(batchId, str(week))
            process_data.append({'skill': skill, 'score': score, 'content': content})
    return process_data

def get_batch_and_associate_spider_data(associate_email, batch_id):
    '''gets associate spider data from an associate email'''
    batch_spider_data = evaluation_service.get_batch_spider_data(batch_id)
    batch_spider_data = json.loads(batch_spider_data)
    for data_dict in batch_spider_data:
        data_dict.pop('traineeId')
        data_dict.pop('weight')
    associate_spider_data = evaluation_service.get_associate_spider_data(batch_id, associate_email)
    associate_spider_data = json.loads(associate_spider_data)
    for data_dict in associate_spider_data:
        data_dict.pop('traineeId')
        data_dict.pop('weight')
    return batch_spider_data, associate_spider_data
