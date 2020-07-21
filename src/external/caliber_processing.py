'''this module is the driver that calls and processes from caliber'''

from src.external import evaluation_service, category_service, evaluation_service, qc_service
from src.logging.logger import get_logger
_log = get_logger(__name__)


def get_qc_data(associate_id):
    '''this function gets qc data from caliber'''
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
