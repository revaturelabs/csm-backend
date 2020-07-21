'''this module is the driver that calls and processes from caliber'''

import datetime
from src.external import training_service, category_service, evaluation_service, qc_service
from src.models.associates import Associate


def get_qc_data(associate_id):
    '''this function gets qc data from caliber'''
    notes = qc_service.get_note_headers(associate_id)
    process_data = []
    for note in notes:
        content = note['content']
        score = note['technicalStatus']
        week = note['week']
        batchId = note['batchId']
        skill = qc_service.get_qc_category(batchId, week)
        process_data.append({})

def get_new_graduates():
    '''associates, end date, batchid'''
    batches = training_service.batch_current()
    current_run = datetime.datetime.today()
    next_run = current_run + datetime.timedelta(days=7)
    assocArr = []
    for batch in batches:
        end_date = datetime.datetime.strptime(batch['endDate'], '%Y-%m-%d')
        if current_run < end_date < next_run:
            batch_id = batch['batchId']
            for assoc in batch['associateAssignments']:
                temp = assoc['associate']
                assocArr.append(Associate(str(temp['salesforceId']), str(temp['email']),
                                          str(batch_id), end_date=end_date))
    return assocArr
